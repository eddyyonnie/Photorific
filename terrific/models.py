from django.db import models

class Location(models.Model): 
    
    location_name=models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

class Category(models.Model):

    category_name=models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class Photo(models.Model):
    photo_name=models.CharField(max_length=30)
    image=models.ImageField(upload_to = 'images/')
    short_description=models.CharField(max_length=500)
    location=models.ForeignKey(Location)
    category=models.ForeignKey(Category)

    def __str__(self):
        return self.photo_name
# Create your models here.
    @classmethod
    def filter_by_location(cls):
        photos = Photo.objects.order_by('location')
        return photos
    @classmethod
    def search_image(cls, search_category):
        images = cls.objects.filter(category__category_name__icontains=search_category)
        return images