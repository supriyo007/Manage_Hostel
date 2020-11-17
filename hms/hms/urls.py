from django.contrib import admin
from django.urls import path
from login_section import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
]
