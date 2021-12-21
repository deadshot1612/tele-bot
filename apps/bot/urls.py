from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path(f'{settings.BOT_TOKEN}/', views.handle)
]