
from django.urls import path
from .views import PhotoList, PhotoCreate, PhotoDelete, PhotoDetail, PhotoUpdate

app_name = "photo"
urlpatterns = [


    path('', PhotoList.as_view(), name='index'),
]
