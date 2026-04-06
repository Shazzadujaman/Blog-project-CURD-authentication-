from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(request):
    if request.method=="POST":
     post_form=forms.Post_form(request.POST)
     if post_form.is_valid():
        post = post_form.save(commit=False)   
        post.author = request.user            
        post.save()
        post_form.save_m2m()  
        return redirect('profile')
    else:
       post_form=forms.Post_form() 

    return render(request,"add_posts.html",{'form': post_form})

@login_required
def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    post_form=forms.Post_form(instance=post)

    if request.method=="POST":
     post_form=forms.Post_form(request.POST, instance=post)
     if post_form.is_valid():
        post_form.save()
        return redirect('profile')

    return render(request,"add_posts.html",{'form':post_form})

@login_required
def delete_post(request,id):
   post=models.Post.objects.get(pk=id)
   post.delete()
   return redirect('profile')

@login_required
def post_detail(request, pk):
    post=get_object_or_404(models.Post, pk=pk)
    comments=post.comments.all()

    form=forms.CommentForm()

    if request.method=='POST':
       if request.user.is_authenticated:
          form=forms.CommentForm(request.POST)
          if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=pk)
          
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })    


def like_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)

    if request.user in post.likes.all():
        post.likes.remove(request.user)  # unlike
    else:
        post.likes.add(request.user)     # like

    return redirect('post_detail', pk=pk)