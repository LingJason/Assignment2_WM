from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRenterForm
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
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      messages.success(request, 'You Have Successfully Registered')
      return redirect('home')
    
  else:
    form = SignUpForm()
    return render(request, 'register.html', {'form': form})
  
  return render(request, 'register.html', {'form': form})

def renter_info(request, pk):
  if request.user.is_authenticated:
    info_renter = Renter.objects.get(id=pk)
    return render(request, 'renter.html', {'info_renter': info_renter})
  
  else:
    messages.success(request, "You Have To Login First")
    return redirect('home')

def verify_logout(request):
  logout(request)
  messages.success(request, "You Have Successfully Logged Out")
  return redirect('home')

def add_renter(request):
  form = AddRenterForm(request.POST or None)
  if request.user.is_authenticated:
    if request.method == "POST":
      if form.is_valid():
        add_renter = form.save()
        messages.success(request, "You Have Successfully Added A New File")
        return redirect('home')
    return render(request, 'add_renter.html', {'form': form})
  else:
    messages.success(request, "You Have To Login First")
    return redirect('home')
  

def update_renter(request, pk):
  if request.user.is_authenticated:
    current_renter = Renter.objects.get(id=pk)
    form = AddRenterForm(request.POST or None, instance= current_renter)
    if form.is_valid():
      form.save()
      messages.success(request, "You Have Updated A File")
      return redirect('home')
    return render(request, 'update_renter.html', {'form':form})
  else:
    messages.success(request, "You Have To Login First")
    return redirect('home')




def delete_renter(request, pk):
  if request.user.is_authenticated:
    delete_info = Renter.objects.get(id=pk)
    delete_info.delete()
    messages.success(request, "You Have Successfully Delete A File")
    return redirect('home')
  else:
    messages.success(request, "Permission Denied")
    return redirect('home')