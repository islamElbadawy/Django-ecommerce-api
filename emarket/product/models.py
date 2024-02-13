from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.TextChoices):
    ELECTRONICS = 'Electronics'
    BOOKS = 'Books'
    CLOTHING_SHOES_AND_JEWELRY = 'Clothing, Shoes, and Jewelry'
    HOME_AND_KITCHEN = 'Home and Kitchen'
    TOYS_AND_GAMES = 'Toys and Games'
    HEALTH_AND_HOUSEHOLD = 'Health and Household'
    SPORTS_AND_OUTDOORS = 'Sports and Outdoors'
    AUTOMOTIVE = 'Automotive'
    BEAUTY_AND_PERSONAL_CARE = 'Beauty and Personal Care'
    GROCERY_AND_GOURMET_FOOD = 'Grocery and Gourmet Food'
    TOOLS_AND_HOME_IMPROVEMENT = 'Tools and Home Improvement'
    BABY_PRODUCTS = 'Baby Products'
    PET_SUPPLIES = 'Pet Supplies'


class Product(models.Model):
    name = models.CharField(max_length=200, default="", blank=False)
    description = models.TextField(max_length=1000, default="", blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=7, default=0)
    brand = models.CharField(max_length=200, default="", blank=False)
    category = models.CharField(max_length=40, choices=Category.choices)
    rating = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    stock = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(decimal_places=2, max_digits=3, default=0)
    comment = models.TextField(max_length=100, default="",blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment
