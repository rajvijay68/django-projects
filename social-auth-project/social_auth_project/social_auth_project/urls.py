from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from core import views as core_views

urlpatterns = [
	path(r'',core_views.home,name='home'),
	path(r'login/',auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
	path(r'logout/',auth_views.LogoutView.as_view(template_name='core/logout.html'),name='logout'),
	path(r'oauth/',include('social_django.urls',namespace='social')),
	path(r'admin/',admin.site.urls),

]