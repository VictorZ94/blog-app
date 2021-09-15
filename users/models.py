from django.contrib.auth.models import User
from django.db import models


class myUser(models.Model):
    """Profile Model

    proxy model that extends the base with another
    information
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=0)

    def __str__(self):
        return self.user.username
