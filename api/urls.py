from django.urls import path,include
from . import views
from .views import Postviewset,RegisterView,Locationviewset,Breedviewset,Categoryviewset,Userviewset,Commentviewset,Replyviewset
from rest_framework.routers import DefaultRouter
#
router=DefaultRouter()
router.register('api_post',Postviewset)
router.register('api_breed',Breedviewset)
router.register('api_category',Categoryviewset)
router.register('api_location',Locationviewset)
router.register('api_user',Userviewset)
router.register('api_comment',Commentviewset)
router.register('api_reply',Replyviewset)



urlpatterns = [
    path('register/',RegisterView.as_view ),
    path('', include(router.urls)),
    # breed
    # ------------------------------------------
    path('breeds/',views.get_data_breeds ),
    path('breeds/<str:pk>/',views.get_data_breed ),
    path('breed/create/',views.create_breed ),
    path('breed/<str:pk>/update/',views.update_breed ),
    path('breed/<str:pk>/delete/',views.delete_breed ),
    # post
    # -------------------------------------------
    path('posts/',views.get_data_posts ),
    path('posts/<str:pk>/',views.get_data_post ),
    path('post/create/',views.create_post ),
    path('posts/<str:pk>/update/',views.update_post ),
    path('posts/<str:pk>/delete/',views.delete_post ),
    # category
    # -----------------------------------------------
    path('categories/',views.get_data_Categories ),
    path('categories/<str:pk>/',views.get_data_Category ),
    path('category/create/',views.create_category ),
    path('categories/<str:pk>/update/',views.update_category ),
    path('categories/<str:pk>/delete/',views.delete_Category ),
    # location
    # ---------------------------------------------------
    path('locations/',views.get_data_locations ),
    path('locations/<str:pk>/',views.get_data_location ),
    path('location/create/',views.create_location ),
    path('locations/<str:pk>/update/',views.update_location ),
    path('locations/<str:pk>/delete/',views.delete_location ),


]
