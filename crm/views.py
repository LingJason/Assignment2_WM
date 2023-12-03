from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Renter

# Create your views here.
def home(request):
  renters = Renter.objects.all()

  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, "Logged In")
      return redirect('home')
    
    else:
      messages.success(request, "Please Try Again")
      return redirect('home')

  else:
    return render(request, 'home.html', {'renters': renters})
  
def register_user(request):

  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.clean_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      messages.success(request, 'You have Successfully Registered')
      return redirect('home')
    
  else:
    form = SignUpForm()
    return render(request, 'register.html', {'form': form})
  
  return render(request, 'register.html', {'form': form})

def renter(request, pk):
  if request.user.is_authenticated:
    renter = Renter.objects.get(id=pk)
    return render(request, 'renter.html', {'renter': renter})
  
  else:
    messages.success(request, "You Have to Login First")
    return redirect('home')

def verify_logout(request):
  logout(request)
  messages.success(request, "You Have Successfully Logged Out")
  return redirect('home')

def delete_renter(request, pk):
  if request.user.is_authenticated:
    delete_info = Renter.objects.get(id=pk)
    delete_info.delete()
    messages.success(request, "You Have Successfully Delete a File")
    return redirect('home')
  else:
    messages.success(request, "Permission Denied")
    return redirect('home')