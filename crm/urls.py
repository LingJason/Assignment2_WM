from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.verify_login, name='login'),
    # path('logout/', views.verify_logout, name='logout'),
]