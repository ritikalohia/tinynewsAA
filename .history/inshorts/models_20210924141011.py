from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    news_author =models.CharField(max_length=50, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cover = models.ImageField(upload_to='images/', default="icon8image.png")
    content_link = models.CharField(max_length=300, unique=True)
    news_publish= models.CharField(max_length=100, unique=True)

class Meta:
    ordering = ['created_on']    

def __str__(self):
    return self.title    