from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo


class PhotoListView(ListView):
    model = Photo
