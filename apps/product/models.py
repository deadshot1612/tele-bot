from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    img = models.ImageField(upload_to ="Images/")
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    catagory = models.ForeignKey(Category, on_delete=models.CASCADE)


