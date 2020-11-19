from django.conf.urls import url, include
from django.urls import path
from users import views

urlpatterns = [
    url(r"^dashboard/", views.dashboard, name="dashboard"),
    url(r"^accounts/", include('django.contrib.auth.urls')),
]