# django
from django.db import models
from django.utils import timezone

# Models django
from django.contrib.auth.models import User

# models
from users.models import myUser


CATEGORY = (
    ("TECH", "tech"),
    ("SCIENCE", "science"),
    ("IOT", "iot"),
    ("AI", "ai"),
)

class Post(models.Model):
    """ define models to save all posts
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)    
    content = models.TextField(blank=True)

    # url field
    slug = models.SlugField(max_length=200, unique=True)

    category = models.CharField(choices=CATEGORY, default="science", 
                                max_length=20)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Likes(models.Model):
    user = models.ForeignKey(myUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


# class Comments(models.Model):
#     user = models.ForeignKey(myUser, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     comment = models.TextField(max_length=200, required=True)



class BlogComment(models.Model):
    blogpost = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)

    user = models.ForeignKey(myUser, on_delete=models.CASCADE)
    content = models.TextField(null=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blogpost.title[:40]
