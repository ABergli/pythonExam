from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
    path('post/new/', views.blog_post_create, name='blog_post_create'),
    path('post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('post/<int:pk>/edit/', views.blog_post_edit, name='blog_post_edit'),
    path('post/<int:pk>/delete/', views.blog_post_delete, name='blog_post_delete'),
]
