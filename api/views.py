from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category,Location,Breed,Post,Comment,Reply,User
from .serializers import LocationSerializer,BreedSerializer,PostSerializer,CategorySerializer,UserSerializer,CommentSerializer,ReplySerializer
from rest_framework import viewsets
from rest_framework.views import APIView

# Create your views here.
class Postviewset(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
# ----------------------------------------------------
class Breedviewset(viewsets.ModelViewSet):
    queryset=Breed.objects.all()
    serializer_class=BreedSerializer
# ----------------------------------------------------
class Locationviewset(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer
# ----------------------------------------------------
class Userviewset(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
# ----------------------------------------------------
class Commentviewset(viewsets.ModelViewSet):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
# ----------------------------------------------------
class Replyviewset(viewsets.ModelViewSet):
    queryset=Reply.objects.all()
    serializer_class=ReplySerializer
# ----------------------------------------------------
class Categoryviewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
# ----------------------------------------------------
# Locations :
# all locations
# --------------------------------------------------------------
@api_view(['GET'])
def get_data_locations(request):
    locations=Location.objects.all()
    serializer=LocationSerializer(locations,many=True)
    return Response(serializer.data)
# specific location
# --------------------------------------------------------------
@api_view(['GET'])
def get_data_location(request,pk):
    location=Location.objects.get(id=pk)
    serializer=LocationSerializer(location,many=False)
    return Response(serializer.data)
# delete location
# --------------------------------------------------------------
@api_view(['DELETE'])
def delete_location(request,pk):
    location=Location.objects.get(id=pk)
    location.delete()
    return Response('location was deleted !')
# create location
# --------------------------------------------------------------
@api_view(['POST'])
def create_location(request):
    data=request.data
    location=Location.objects.create(
        locationName=data['locationName']
    )
    serializer=LocationSerializer(location,many=False)
    return Response(serializer.data)
# update location
# --------------------------------------------------------------
@api_view(['PUT'])
def update_location(request,pk):
    data=request.data
    location=Location.objects.get(id=pk)
    serializer=LocationSerializer(location,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# -------------------------------------------------------------------------------------

# Categories :
# all categories
# --------------------------------------------------------------
@api_view(['GET'])
def get_data_Categories(request):
    Categories=Category.objects.all()
    serializer=CategorySerializer(Categories,many=True)
    return Response(serializer.data)
# specific category
# -----------------------------------------------------------------
@api_view(['GET'])
def get_data_Category(request,pk=id):
    Category=Category.objects.get(id=pk)
    serializer=CategorySerializer(Category,many=False)
    return Response(serializer.data)
# delete category
# -----------------------------------------------------------------
@api_view(['DELETE'])
def delete_Category(request,pk=id):
    Category=Category.objects.get(id=pk)
    Category.delete()
    return Response('category was deleted !')
# create category
# -----------------------------------------------------------------
@api_view(['POST'])
def create_category(request):
    data=request.data
    Category=Category.objects.create(
        name=data['name']
    )
    serializer=LocationSerializer(Category,many=False)
    return Response(serializer.data)
# Update category
# -----------------------------------------------------------------
@api_view(['PUT'])
def update_category(request,pk=id):
    data=request.data
    Category=Category.objects.get(id=pk)
    serializer=LocationSerializer(Category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# -------------------------------------------------------------------------------------
# BREEDS :
# all breeds
# ------------------------------------------------------------------
@api_view(['GET'])
def get_data_breeds(request):
    breeds=Breed.objects.all()
    serializer=BreedSerializer(breeds,many=True)
    return Response(serializer.data)
# specific breed
# ------------------------------------------------------------------
@api_view(['GET'])
def get_data_breed(request,pk):
    breed=Breed.objects.get(id=pk)
    serializer=BreedSerializer(breed,many=False)
    return Response(serializer.data)
# delete breed
# ------------------------------------------------------------------
@api_view(['DELETE'])
def delete_breed(request,pk):
    breed=Breed.objects.get(id=pk)
    breed.delete()
    return Response('breed was deleted !')
# create breed
# ------------------------------------------------------------------
@api_view(['POST'])
def create_breed(request):
    data=request.data
    breed=Breed.objects.create(
        breed=data['breed'],
        category_type=data['category_type']
    )
    serializer=LocationSerializer(breed,many=False)
    return Response(serializer.data)
# Update breed
# ------------------------------------------------------------------
@api_view(['PUT'])
def update_breed(request,pk=id):
    data=request.data
    breed=Breed.objects.get(id=pk)
    serializer=LocationSerializer(breed, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# -------------------------------------------------------------------------------------
# Posts
# all posts
# ------------------------------------------------------------------
@api_view(['GET'])
def get_data_posts(request):
    posts=Post.objects.all()
    serializer=PostSerializer(posts,many=True)
    return Response(serializer.data)

#specific posts
# ------------------------------------------------------------------
@api_view(['GET'])
def get_data_post(request,pk):
    post=Post.objects.get(id=pk)
    serializer=PostSerializer(post,many=False)
    return Response(serializer.data)
# delete post
# ------------------------------------------------------------------
@api_view(['Delete'])
def delete_post(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return Response('post was deleted !')


# create post
# ------------------------------------------------------------------
@api_view(['POST'])
def create_post(request):
    data=request.data
    post=Post.objects.create(
        name=data['name'],
        desc=data['desc'],
        image=data['image'],
        category_id=data['category_id'],
        loction_pet=data['loction_pet'],
    )
    serializer=LocationSerializer(post,many=False)
    return Response(serializer.data)

# Update post
# ------------------------------------------------------------------
@api_view(['PUT'])
def update_post(request,pk=id):
    data=request.data
    post=Post.objects.get(id=pk)
    serializer=LocationSerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
# users
# register
# ------------------------------------------------------------------
class RegisterView(APIView):
    def post(self,request):
        pass
