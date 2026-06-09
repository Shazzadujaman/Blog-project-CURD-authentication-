from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts import models
# Create your views here.

def register(request):
   if request.method=="POST":
     registration_form=forms.RegistrationForm(request.POST)
     if registration_form.is_valid():
        user=registration_form.save()
        role=registration_form.cleaned_data.get('role')
        user.profile.role=role
        user.profile.save()
        login(request,user)
        messages.success(request,'Registration Successful')
        return redirect('home')
   else:
       registration_form=forms.RegistrationForm() 

   return render(request,"registration.html",{'form':registration_form , 'type':'Resgistration'})

def user_login(request):
   if request.method=='POST':
      form=AuthenticationForm(data=request.POST)
      if form.is_valid():
         user_name=form.cleaned_data.get('username')
         password=form.cleaned_data.get('password')

         user=authenticate(username=user_name,password=password)

         if user is not None:
            messages.success(request,'Log in successful')
            login(request,user)
            return redirect('home')
         
         else:
             messages.warning(request,'Log in Failed')
             return redirect('home')

         
   else:
      form=AuthenticationForm()
   return render(request,'registration.html',{'form':form , 'type':'LogIn'}) 

@login_required
def profile(request):
   data=models.Post.objects.filter(author=request.user)
   return render(request,'profile.html',{'data':data})   

@login_required
def edit_profile(request):
   if request.method=='POST':
      form=forms.EditProfile(request.POST,instance=request.user)
      if form.is_valid():
         messages.success(request,'Profile edit successful')
         user=form.save()
         role=form.cleaned_data.get('role')
         user.profile.role=role
         user.profile.save()
         return redirect('profile')
   else:
      form=forms.EditProfile(instance=request.user)
   return render(request,'edit_profile.html',{'form':form})       

@login_required
def pass_change(request):
   if request.method=='POST':
      form=PasswordChangeForm(user=request.user , data=request.POST)
      if form.is_valid():
         messages.success(request,'Password Changed successfuly')
         form.save()
         return redirect('profile')
   else:
      form=PasswordChangeForm(user=request.user)
   return render(request,'pass_change.html',{'form':form})

@login_required
def user_logout(request):
   logout(request)
   return redirect('login')

@login_required
def manage_users(request):
   if not hasattr(request.user, 'profile') or request.user.profile.role != 'super_admin':
      messages.error(request, "Access denied. Only Super Admin can manage users.")
      return redirect('profile')
   
   from django.contrib.auth.models import User
   users = User.objects.all().select_related('profile')
   return render(request, 'manage_users.html', {'users': users})

@login_required
def delete_user(request, user_id):
   if not hasattr(request.user, 'profile') or request.user.profile.role != 'super_admin':
      messages.error(request, "Access denied. Only Super Admin can delete users.")
      return redirect('profile')
   
   from django.contrib.auth.models import User
   try:
      user_to_delete = User.objects.get(pk=user_id)
      if user_to_delete == request.user:
         messages.warning(request, "You cannot delete your own account.")
      else:
         username = user_to_delete.username
         user_to_delete.delete()
         messages.success(request, f"User '{username}' was successfully deleted.")
   except User.DoesNotExist:
      messages.error(request, "User not found.")
   
   return redirect('manage_users')