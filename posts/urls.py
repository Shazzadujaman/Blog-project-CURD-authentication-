from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.add_post,name='add_post'),
    path('edit/<int:id>',views.edit_post,name='edit_post'),
    path('delete/<int:id>',views.delete_post,name='delete_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),

]