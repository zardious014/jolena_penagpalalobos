from django.urls import path
from . import views
from .views import create_user, user_list, update_user, delete_user

urlpatterns = [
    path('', views.index, name="home_page"),
    path('aboutpage/', views.aboutPage, name="about_page"),
    path('contactpage/', views.contactPage, name="contact_page"),
    path('catlist/', views.catList, name="cat_buddies"),
    path('create_user/', create_user, name='create_user'),
    path('user-list/', user_list, name='user_list'),
    path('update-user/<int:pk>/', update_user, name='update_user'),
    path('delete-user/<int:pk>/', delete_user, name='delete_user'),
    
  
]
