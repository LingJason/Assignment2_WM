from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):

  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(request, username=email, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, "Logged In")
      return redirect('home')
    
    else:
      messages.success(request, "Please Try Again")
      return redirect('home')

  else:
    return render(request, 'home.html', {})

# def verify_login(request):
#   pass

# def verify_logout(request):
#   pass