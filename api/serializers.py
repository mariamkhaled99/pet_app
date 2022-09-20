
from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Category,Location,Breed,Post,Comment,Reply,User



class CategorySerializer(ModelSerializer):

    class Meta:
        model=Category
        fields='__all__'
class LocationSerializer(ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'
class BreedSerializer(ModelSerializer):
    class Meta:
        model=Breed
        fields='__all__'
class PostSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'

class ReplySerializer(ModelSerializer):
    class Meta:
        model=Reply
        fields='__all__'
class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
