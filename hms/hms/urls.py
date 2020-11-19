from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
# from django.contrib.auth import views as auth_views
from login_section import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup/', views.signup, name='signup'),
    # path('', views.home, name='home'),
    # # path('login/',auth_views.LoginView.as_view(template_name='login.html'), name='loggedin'),
    # path('login/',views.loggedin, name='loggedin'),
    url(r'^',include('users.urls')),
]
