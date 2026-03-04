from django.contrib import admin
from django.urls import include, path  # include ekli olmalı

urlpatterns = [
    path("polls/", include("polls.urls")),  # polls/urls.py'yi dahil ediyor
    path("admin/", admin.site.urls),
]