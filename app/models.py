from django.db import models

# Create your models here.



class Category (models.Model) :
    name = models.CharField(max_length=100)

    def __str__(self) :
        return f"{self.name}"


class Film (models.Model) :
    name = models.CharField(max_length=1000)
    des = models.TextField(max_length=5000,null=True)
    image = models.TextField(max_length=5000,null=True)
    url = models.TextField(max_length=1000,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    kind = models.ForeignKey(Category,related_name='film_category',on_delete=models.CASCADE,null=True)
    trend = models.BooleanField(default=False)

    def __str__ (self) :
        return f"{self.name}"


class Search (models.Model) :
    name = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__ (self) : return f"{self.name} "


class Series (models.Model) :
    name = models.CharField(max_length=1000)
    image = models.TextField(max_length=2000)
    desc = models.TextField(max_length=5000)
    trend = models.BooleanField(default=False)

    def __str__(self) :
        return self.name


class Series_Part (models.Model) :
    series = models.ForeignKey(Series,related_name='for_series',on_delete=models.CASCADE)
    url = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=500,null=True)
    def __str__(self) :
        return f"{self.title}"
