from django.db import models


class Category(models.Model):
    parent = models.ForeignKey("self",
        null=True,
        blank=True,
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class SupplementaryContent(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class RegulationSection(models.Model):
    title = models.CharField(max_length=16)
    part = models.CharField(max_length=16)
    subpart = models.CharField(max_length=32, null=True, blank=True)
    section = models.CharField(max_length=16)
    supplementary_content = models.ManyToManyField(SupplementaryContent, related_name="sections")

    def __str__(self):
        return f'{self.title} {self.part}.{self.section}'
