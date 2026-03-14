from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_catagories(request):
    if request.method=="POST":
     catagories_form=forms.Catagories_form(request.POST)
     if catagories_form.is_valid():
        catagories_form.save()
        return redirect('add_catagories')
    else:
       catagories_form=forms.Catagories_form() 

    return render(request,"add_catagories.html",{'form': catagories_form})