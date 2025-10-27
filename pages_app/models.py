from django.db import models

# Create your models here.
class message(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

class Post(models.Model):
    title = models.CharField(max_length=200)
    topic = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)

    def __str__(self):
        return self.title