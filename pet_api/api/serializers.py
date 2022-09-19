
from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer
from .models import Category,Location,Breed,Post



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
    
    
    
