from django.shortcuts import render
from apps.product.models import Category
# Create your views here.


def all_categories():
    categories = Category.objects.all()
    return categories