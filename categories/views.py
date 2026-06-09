<<<<<<< HEAD
from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def add_categories(request):
    if request.method=="POST":
     categories_form=forms.Categories_form(request.POST)
     if categories_form.is_valid():
        categories_form.save()
        messages.success(request, "Category added successfully.")
        return redirect('add_categories')
    else:
       categories_form=forms.Categories_form() 

    categories = models.Categories.objects.all()
    return render(request,"add_categories.html",{'form': categories_form, 'categories': categories})

@login_required
def delete_category(request, id):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'super_admin':
        messages.error(request, "Access denied. Only Super Admin can delete categories.")
        return redirect('home')
        
    try:
        category = models.Categories.objects.get(pk=id)
        name = category.name
        category.delete()
        messages.success(request, f"Category '{name}' was successfully deleted.")
    except models.Categories.DoesNotExist:
        messages.error(request, "Category not found.")
        
    return redirect('add_categories')
=======
from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_categories(request):
    if request.method=="POST":
     categories_form=forms.Categories_form(request.POST)
     if categories_form.is_valid():
        categories_form.save()
        return redirect('add_categories')
    else:
       categories_form=forms.Categories_form() 

    return render(request,"add_categories.html",{'form': categories_form})
>>>>>>> abdfa808ff13bfb59dc6fe4fc61a6cb9fe1b8fbb
