# All imports
from django.shortcuts import render
from django.http import response, JsonResponse
from django.db.models import Q
import os, io
from google.cloud import vision
import cloudinary
import cloudinary.uploader
import cloudinary.api
from bare_test_api.settings import env
from api.models import Photo
import asyncio

# Configuring Cloudinary
cloudinary.config(
    cloud_name = env('CLOUDINARY_CLOUD_NAME'),
    api_key = env('CLOUDINARY_API_KEY'),
    api_secret = env('CLOUDINARY_SECRET')
)

# Upload Image
def uploadImage(request):
    
    # Make sure it is a POST request
    if request.method == "POST":
        
        # Try to upload image
        try:
            # Store image received in a variable
            imageData = request.FILES['imageData']

            # Upload to cloudinary folder
            res = cloudinary.uploader.upload(imageData, folder="bare-app")

            # Instantiate client
            client = vision.ImageAnnotatorClient()
            image = vision.Image()

            # Set the Image URI to the secure URL from Cloudinary
            image.source.image_uri = res['secure_url']

            # Insatntiate the face detection process
            response = client.face_detection(image=image)
            
            # Check for a face/faces on the response
            faces = response.face_annotations

            # If the image has at least a face
            if len(faces) > 0:

                # Sync with DB
                image = Photo(name=res['secure_url'], has_face=True)
                image.save()
                
                # Return response
                return JsonResponse({
                    "success": "File uploaded",
                    "faces" : len(faces)
                })
            else:
                # Return an error message
                return JsonResponse({
                    "error": "Image does not contain a face or faces"
                })
        except:
            # Returns an error message if upload was not completed
            return JsonResponse({
                "error" : "An error occured"
            })
    
    return JsonResponse({
        "page_name" : "uploadPage"
    })

# Get all Images
def getImages(request):
    # Get images that are links
    images = Photo.objects.filter(Q(name__contains='http') & Q(is_deleted=False))
    
    # Add each link to an array 
    image_URLs = []
    for image in images:
        # Create an object for each image Data
        single_image = {}

        # Add image data to the object
        single_image['id'] = image.id
        single_image['name'] = image.name

        # Append the object 
        image_URLs.append(single_image)

    # Send the array as a response 
    return JsonResponse({
        "images" : image_URLs
    })

# Delete Image Endpoint
def deleteImage(request, id):
    if request.method == "DELETE":
        # Get image with ID
        image = Photo.objects.get(pk=id)

        # Set is_deleted field to True and save
        image.is_deleted = True
        image.save()
        
        # Return a response message
        return JsonResponse({
            "message": "Image deleted",
            "id" : id
        })
    