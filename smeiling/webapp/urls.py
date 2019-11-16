from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r"^$", views.home, name="home"),
    url(r"^about/$", views.about, name="about"),
    url(r"^dashboard/(?P<name>[^/]+)/$", views.dashboards, name="dashboards"),
]

urlpatterns = [url(r"^vodademo/", include(urlpatterns))]
