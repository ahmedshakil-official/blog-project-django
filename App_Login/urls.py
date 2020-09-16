from django.urls import path
from .views import *


app_name = 'App_Login'

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('password/', pass_change, name='change_password'),
    path('add_profile_pic/', add_pro_pic, name='add_pro_pic'),
    path('change_profile_pic/', change_pro_pic, name='change_pro_pic'),
]

