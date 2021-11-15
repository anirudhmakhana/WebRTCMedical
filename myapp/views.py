from django.shortcuts import render
import os

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')