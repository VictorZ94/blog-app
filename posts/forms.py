from django.forms import ModelForm
from .models import Post
from .models import BlogComment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']



class NewCommentForm(ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']
