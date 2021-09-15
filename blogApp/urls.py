"""blogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts import views as posts_views
from users import views as users_views

urlpatterns = [
    path('', posts_views.root, name="root"),
    path('posts/', posts_views.list_posts, name='post'),
    path('posts/read_post/<int:post_id>/<int:author_id>/<str:slug>',
          posts_views.read_post, name='read'),
    path('posts/edit_post/<str:slug>', posts_views.edit_post, name='edit'),
    path('posts/create_post/', posts_views.create_post, name='create'),
    path('posts/author_posts/<str:author_id>', posts_views.author_posts, name='author'),
    path('posts/delete_post/<str:id>', posts_views.delete_post, name='delete'),

    # User's path
    path('login/', users_views.login_view, name='login'),
    path('signup/', users_views.signup_view, name='signup'),
    path('logout/', users_views.logout_view, name='logout'),

    # path like
    path('like/<int:post_id>/<int:author_id>/', posts_views.like, name="like"),

    # path to delete comment
    path('del_comment/<int:post_id>/<int:author_id>/<str:slug>/<int:comment_id>/', 
          posts_views.delete_comment, name="del_comment"),
]
