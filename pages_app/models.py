from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class message(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Post(models.Model):
    title = models.CharField(max_length=200)
    topic = models.TextField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title