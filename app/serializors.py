from rest_framework import serializers
from .models import Film, Category



class FilmSer (serializers.ModelSerializer) :
    class Meta:
        model = Film
        fields = ['id','name','image','trend']

class CategorySer (serializers.ModelSerializer) :
    class Meta:
        model = Category
        fields = ['name']

