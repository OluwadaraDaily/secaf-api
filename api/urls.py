from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.uploadImage, name="upload"),
    path('get_images', views.getImages, name="get_images"),
    path('delete/<int:id>', views.deleteImage, name="delete_image"),
]