from django.contrib import admin
from django.urls import path
from password import views
app_name = 'password_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('special/', views.special, name='special')
]
