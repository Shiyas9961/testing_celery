from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main_app.urls")),
    path("upload/", include("csv_app.urls")),
]
