from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from .models import User

def index(request):
    return render(request, 'pages/homepage.html')

def aboutPage(request):
    return render(request, 'pages/aboutpage.html')

def contactPage(request):
    return render(request, 'pages/contactpage.html')

def catList(request):
    return render(request, 'pages/catlist.html')

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'pages/create_user.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'pages/user_list.html', {'users': users})


def update_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'pages/update_user.html', {'form': form})

def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'pages/delete_user.html', {'user': user})

