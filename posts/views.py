from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
from django.contrib import messages

=======
>>>>>>> abdfa808ff13bfb59dc6fe4fc61a6cb9fe1b8fbb
# Create your views here.
@login_required
def add_post(request):
    if request.method=="POST":
     post_form=forms.Post_form(request.POST)
     if post_form.is_valid():
<<<<<<< HEAD
        post = post_form.save(commit=False)   # ❗ important
        post.author = request.user            # ✅ set logged-in user
=======
        post = post_form.save(commit=False)   
        post.author = request.user            
>>>>>>> abdfa808ff13bfb59dc6fe4fc61a6cb9fe1b8fbb
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
<<<<<<< HEAD
   try:
      post=models.Post.objects.get(pk=id)
      # Check permissions
      is_author = post.author == request.user
      is_moderator = hasattr(request.user, 'profile') and request.user.profile.role == 'moderator'
      is_superadmin = hasattr(request.user, 'profile') and request.user.profile.role == 'super_admin'
      
      if is_author or is_moderator or is_superadmin:
         post.delete()
         messages.success(request, "Post deleted successfully.")
      else:
         messages.error(request, "You do not have permission to delete this post.")
   except models.Post.DoesNotExist:
      messages.error(request, "Post not found.")
      
   return redirect('home')

def post_detail(request, id):
    try:
        post = models.Post.objects.get(pk=id)
    except models.Post.DoesNotExist:
        messages.error(request, "Post not found.")
        return redirect('home')
        
    comments = post.comments.all().order_by('-created_at')
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to comment.")
            return redirect('login')
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Comment added successfully.")
            return redirect('post_detail', id=post.id)
    else:
        comment_form = forms.CommentForm()
        
    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def delete_comment(request, id):
    try:
        comment = models.Comment.objects.get(pk=id)
        post_id = comment.post.id
        
        # Check permissions
        is_author = comment.author == request.user
        is_moderator = hasattr(request.user, 'profile') and request.user.profile.role == 'moderator'
        is_superadmin = hasattr(request.user, 'profile') and request.user.profile.role == 'super_admin'
        
        if is_author or is_moderator or is_superadmin:
            comment.delete()
            messages.success(request, "Comment deleted successfully.")
        else:
            messages.error(request, "You do not have permission to delete this comment.")
    except models.Comment.DoesNotExist:
        messages.error(request, "Comment not found.")
        return redirect('home')
        
    return redirect('post_detail', id=post_id)

=======
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
>>>>>>> abdfa808ff13bfb59dc6fe4fc61a6cb9fe1b8fbb
