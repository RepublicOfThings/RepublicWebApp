from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    url(r"^$", views.home, name="home"),
    url(r"^about/$", views.about, name="about"),
    url(r"^dashboard/(?P<name>[^/]+)/$", views.dashboard, name="dashboards"),
    path(r"^admin/", admin.site.urls, name="admin")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
