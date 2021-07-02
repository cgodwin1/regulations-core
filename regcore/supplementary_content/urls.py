from django.urls import path

from .views import (
    SupplementaryContentView,
)

urlpatterns = [path("supplemental-content", SupplementaryContentView.as_view()),]
