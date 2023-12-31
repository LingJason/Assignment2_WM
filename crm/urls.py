from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.verify_logout, name='logout'),
    path('register/', views.register_user, name='register'),
    path('add_renter/', views.add_renter, name='add_renter'),
    path('renter/<int:pk>', views.renter_info, name='renter'),
    path('update_renter/<int:pk>', views.update_renter, name='update_renter'),
    path('delete_renter/<int:pk>', views.delete_renter, name='delete_renter'),
]