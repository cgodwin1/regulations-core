from rest_framework import serializers, generics

from .models import (
    Category,
    SupplementaryContent,
    RegulationSection,
)


class SupplementaryContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegulationSection
        fields = ("title", "section")


class SupplementaryContentView(generics.ListAPIView):
    serializer_class = SupplementaryContentSerializer

    def get_queryset(self):
        sections = self.request.GET.getlist("sections")
        query = RegulationSection.objects.filter(section__in=sections)
        return query
