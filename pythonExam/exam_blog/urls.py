from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from blog import views

app_name = 'blog'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    path('post/new/', views.blog_post_create, name='blog_post_create'),
    path('post/<int:pk>/edit/', views.blog_post_edit, name='blog_post_edit'),
    path('post/<int:pk>/delete/', views.blog_post_delete, name='blog_post_delete'),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
