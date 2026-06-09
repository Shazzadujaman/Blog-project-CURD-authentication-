from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.add_categories,name='add_categories'),
    path('delete/<int:id>/',views.delete_category,name='delete_category'),
]