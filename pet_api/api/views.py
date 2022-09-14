from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category,Location,Breed,Post
from .serializers import LocationSerializer,BreedSerializer,PostSerializer,CategorySerializer


# Create your views here.

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