from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]