from django.urls import path,include
from . import views

urlpatterns = [
    path('add/',views.add_catagories,name='add_catagories')
]