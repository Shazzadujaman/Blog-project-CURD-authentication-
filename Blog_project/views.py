from django.shortcuts import render
from posts.models import Post
from categories.models import Categories

def home(request,category_slug=None):
    data=Post.objects.all()
    if category_slug is not None:
        category=Categories.objects.get(slug=category_slug)
        data=Post.objects.filter(category=category)

    categories = Categories.objects.all()   

    return render(request,'home.html',{'data':data, 'category' : categories})