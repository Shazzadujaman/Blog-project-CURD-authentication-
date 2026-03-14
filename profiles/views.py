from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add(request):
    if request.method=="POST":
     profile_form=forms.profile_form(request.POST)
     if profile_form.is_valid():
        profile_form.save()
        return redirect('add_profile')
    else:
       profile_form=forms.profile_form() 

    return render(request,"add_profile.html",{'form':profile_form})