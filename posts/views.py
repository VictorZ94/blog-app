from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

# models 
from django.contrib.auth.models import User
from posts.models import Post, Likes, BlogComment
from users.models import myUser

# forms
from .forms import PostForm
from .forms import NewCommentForm


@login_required(login_url='/login/')
def list_posts(request):
    """ view to list existing posts
    """
    if request.method == 'POST':
        category = request.POST.get('category', False)
        posts = Post.objects.select_related('author')\
        .filter(category=category)\
        .order_by('-modified')
        # import pdb; pdb.set_trace()
        return render(request, 'posts/index.html',
                  {'posts': posts})

    posts = Post.objects.select_related('author').order_by('-modified')
    likes = Likes.objects.select_related('post')

    return render(request, 'posts/index.html',
                  {'posts': posts})

@login_required(login_url='/login/')
def read_post(request, post_id, author_id, slug):
    """ view to read the posts
    to receive a slug like arg
    """
    if request.method == 'POST':
        form_comment = request.POST['comment']
        user = myUser.objects.get(id=author_id)
        post = Post.objects.get(id=post_id)
        comment = BlogComment(user=user, blogpost=post)
        comment.content = form_comment
        comment.save()

        post = Post.objects.get(slug=slug)
        comments = BlogComment.objects.filter(blogpost=post_id)
        like = Likes.objects.filter(post_id=post_id)
        return render(request, 'posts/read_post.html',
                      {'comments': comments, 'post': post,'like': like})

    post = Post.objects.get(slug=slug)
    comments = BlogComment.objects.filter(blogpost=post_id)
    like = Likes.objects.filter(post_id=post_id)
    return render(request, 'posts/read_post.html',
                    {'comments': comments, 'post': post, 'like': like })

@login_required(login_url='/login/')
def delete_comment(request, post_id, author_id, slug, comment_id):
    """ delete post comment 
    """
    comment = BlogComment.objects.get(id=comment_id)
    comment.delete()
    return redirect('read', post_id=post_id, 
                    author_id=author_id, slug=slug)

@login_required(login_url='/login/')
def create_post(request):
    """ create and publish blog/post
    """
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user_id = request.POST['author_id']
        category = request.POST['category']

        slug = "-".join(list(map(lambda word: word.lower(), title.split())))
        author = User.objects.get(id=int(user_id))

        # save info in models
        post = Post()
        post.author = author
        post.category = category
        post.title = title
        post.content = content
        post.slug = slug
        post.save()
        return redirect('post')

    return render(request, 'posts/create_post.html')

@login_required(login_url='/login/')
def author_posts(request, author_id):
    """ List existing posts by author
    """
    id = int(author_id)
    user = myUser.objects.get(user_id=id)
    if user.is_admin:
        posts = Post.objects.select_related('author').order_by('-modified')
    else:
        posts = Post.objects.select_related('author').filter(author_id=id).order_by('-modified')

    return render(request, 'posts/authors.html',
                  {'posts': posts})

@login_required(login_url='/login/')
def edit_post(request, slug):
    """ this view allow us modify a post
    """
    post = Post.objects.get(slug=slug)
    # import pdb; pdb.set_trace()
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post')

    return render(request, 'posts/edit.html', {'post': post})

@login_required(login_url='/login/')
def delete_post(request, id):
    """ delete a post
    """
    post = Post.objects.get(id=int(id))
    post.delete()
    return redirect('post')

@login_required(login_url='/login/')
def like(request, post_id, author_id, slug):
    """ button like
    """
    if request.method == 'POST':
        user = myUser.objects.get(id=author_id)
        post = Post.objects.get(id=post_id)
        like = Likes(user=user, post=post)
        like.save()
        return redirect('read', post_id=post_id, 
                        author_id=author_id, slug=slug)

def root(request):
    """ redirect to login
    """
    return redirect('login')
