

from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
# from django.contrib.auth.models import AbstractUser


class Category(models.Model):
    name=models.CharField(max_length=120)
    

    def __str__(self):
        return self.name

    @classmethod
    def get_specific_object(cls,id):
        return get_object_or_404(cls,pk=id)
    
class Breed(models.Model):
    breed=models.CharField(max_length=120)
    category_type=models.ForeignKey(Category, on_delete=models.CASCADE,null=True,related_name='breed_cat')

    def __str__(self):
        return self.breed


# class User (AbstractUser):
#     is_blocked=models.BooleanField(default=False)
#     email= models.EmailField(unique=True)
#     subscribed_categories= models.ManyToManyField(Category, blank=True)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []

#     @classmethod
#     def get_object_or_none(cls, **kwargs):
#         try:
#             return User.objects.get(**kwargs)

#         except User.DoesNotExist:
#             return None


class Location(models.Model):
    locationName=models.CharField(max_length=40)
    
    def __str__(self):
        return self.locationName
    
class Post(models.Model):
    name=models.CharField(max_length=40)
    desc=models.TextField(null=True, max_length=500)

  
    image=models.ImageField(upload_to="images/",null=True)

    created_at=models.DateTimeField(auto_now_add=True,null=True)
    edited_at=models.DateTimeField(auto_now=True)

    # likes=models.ManyToManyField(User, related_name='api_likes', blank=True)
    # adapted=models.ManyToManyField(User, related_name='api_adapted',  blank=True)

    category_id=models.ForeignKey(Category ,on_delete=models.CASCADE,null=True,related_name='cat_posts')
    # user=models.ForeignKey(User ,on_delete=models.CASCADE,null=True,related_name='user_posts')
    loction_pet = models.ForeignKey(Location, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        return f"/media/{self.image}"
 
    @classmethod
    def get_all_object(cls):
        return cls.objects.all()
    
    @classmethod
    def get_specific_object(cls,id):
        return get_object_or_404(cls,pk=id)
    
    def show_url(self):
        return reverse("postinfo",args=[self.id])
    
    def get_all_url(self):
        return reverse("home")
    
    
# class Comment(models.Model):
#     content=models.TextField(max_length=500)
#     created_at=models.DateTimeField(auto_now_add=True,null=True)

#     post=models.ForeignKey(Post ,on_delete=models.CASCADE,null=True,related_name='post_comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

#     def get_replies(self):
#         return self.replies.all()
    
   
# class Reply(models.Model):
#     reply_post=models.ForeignKey(Post ,on_delete=models.CASCADE,null=True,related_name='re_post')
#     comment=models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     content=models.TextField(max_length=500)
#     created_at=models.DateTimeField(auto_now_add=True,null=True)

#     def __str__(self):
#         return self.user.username


