from django.urls import path,include
from . import views

urlpatterns = [
    path('registration/',views.register,name='registration'),
    path('login/',views.user_login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('pass_change/',views.pass_change,name='pass_change'),
    path('logout/',views.user_logout,name='logout'),
    path('manage_users/',views.manage_users,name='manage_users'),
    path('delete_user/<int:user_id>/',views.delete_user,name='delete_user'),
]
