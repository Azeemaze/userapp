from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact_no = models.IntegerField()
    place = models.CharField(max_length=30)

class Post(models.Model):
    Title = models.CharField(max_length=100,null=True)
    Description = models.CharField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    # body = models.TextField()
    # post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorised',null=True)
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()


