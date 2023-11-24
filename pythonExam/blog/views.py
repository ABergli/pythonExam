from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
import logging
from .models import BlogPost
from .forms import BlogPostForm
from .forms import CustomUserCreationForm

logger = logging.getLogger(__name__)


def home(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'blog_posts': blog_posts})

def blog_post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save()
            return redirect('blog:home')
    else:
        form = BlogPostForm()
    return render(request, 'blog/blog_post_form.html', {'form': form})

def blog_post_detail(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog/blog_post_detail.html', {'blog_post': blog_post})

def blog_post_edit(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            blog_post = form.save()
            return redirect('blog_post_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/blog_post_form.html', {'form': form})

def blog_post_delete(request, pk):
    blog_post = get_object_or_404(BlogPost, pk=pk)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('blog:home')
    return render(request, 'blog/blog_post_confirm_delete.html', {'blog_post': blog_post})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            logger.info(f"User {user.username} successfully registered.")
            return redirect('blog:home')
        else:
            logger.error(f"Registration failed. Form errors: {form.errors}")
    else:
        form = CustomUserCreationForm()

    return render(request, 'blog/register.html', {'form': form})