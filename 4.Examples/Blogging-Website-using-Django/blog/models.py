from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Post(models.Model):
    title = models.CharField(max_length = 500)
    content=models.TextField(max_length = 3000)
    header_image = models.ImageField(null = True,blank=True,upload_to = "images/")
    topic= models.CharField(max_length = 50)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    published_date=models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)
    name = models.CharField(max_length= 100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return '%s- %s'% (self.post.title, self.name)
class Profile(models.Model):
    name = models.CharField(max_length= 100)
    bio = models.TextField()
    profile_pic = models.ImageField(null = True,blank=True,upload_to = "images/profile/")
    facebook = models.CharField(max_length = 100, null= True)
    twitter = models.CharField(max_length=100, null=True)
    linkdin = models.CharField(max_length=100, null=True)

    github = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

