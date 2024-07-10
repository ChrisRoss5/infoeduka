"""
URL configuration for Infoeduka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from Infoeduka.settings import BASE_DIR

from django.http import HttpResponse
import os


def check_permissions(request):
    db_path = BASE_DIR / "tmp" / "db.sqlite3"
    db_path2 = "tmp/db.sqlite3"
    db_path3 = os.path.join("/tmp", "db.sqlite3")
    db_path4 = os.path.join("tmp", "db.sqlite3")
    tmp_dir_writable = os.access("tmp", os.W_OK)
    tmp_dir_writable2 = os.access("/tmp", os.W_OK)
    return HttpResponse(
        f'Database {db_path} writable: {os.access(db_path, os.W_OK)} <br> \
          Database {db_path2} writable: { os.access( db_path2, os.W_OK)} <br> \
          Database {db_path3} writable: {os.access(db_path3, os.W_OK)} <br> \
          Database {db_path4} writable: {os.access(db_path4, os.W_OK)} <br> \
          tmp directory writable: {tmp_dir_writable} <br> \
          /tmp directory writable: {tmp_dir_writable2} <br> \
          GAE_ENV: { os.getenv("GAE_ENV", "")}'
    )


urlpatterns = [
    path("", include("main.urls")),
    path("", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("check-permissions/", check_permissions),
]
