from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add(request):
    if request.method=="POST":
     author_form=forms.Author_form(request.POST)
     if author_form.is_valid():
        author_form.save()
        return redirect('add')
    else:
       author_form=forms.Author_form() 

    return render(request,"add_author.html",{'form':author_form})