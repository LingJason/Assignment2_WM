from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.verify_logout, name='logout'),
    path('register/', views.register_user, name='register'),
    path('renter/<int:pk>', views.renter, name='renter'),
    path('delete_renter/<int:pk>', views.delete_renter, name='delete_renter'),
]