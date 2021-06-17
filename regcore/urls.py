"""URLs file for Django. This will inspect the installed apps and only
include the read/write end points that are associated with the regcore_read
and regcore_write apps"""


from collections import defaultdict

from django.conf import settings
from django.utils.module_loading import import_string
from django.urls import path, include

from regcore.urls_utils import by_verb_url #REMOVE

from regcore.views import (
    EffectivePartView,
    EffectiveTitlesView,
    EffectivePartsView,
    EffectivePartTocView,
    PartsView,
)

urlpatterns = [
    path("v2/", include([
        path("", include('regcore.search.urls')),
        path("", PartsView.as_view()),
        path("title/<title>/part/<name>", PartsView.as_view()),
        path("<date>", EffectiveTitlesView.as_view()),
        path("<date>/title/<title>", EffectivePartsView.as_view()),
        path("<date>/title/<title>/part/<name>", EffectivePartView.as_view()),
        path("<date>/title/<title>/part/<name>/toc", EffectivePartTocView.as_view()),
    ]))
]