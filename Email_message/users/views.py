from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm')

        if confirm_password == password:
            user = User.objects.create(first_name=first, last_name=last, email=email, username=username)
            user.set_password(password)
            user.save()
        messages.success(request, f'Your account has been successfully registered!')
        return redirect('login')
    return render(request, 'users/register.html', {'check': True})


@login_required()
def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


@login_required()
def delete(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':

        user.delete()
        return redirect('index')
    return render(request, 'delete.html', {'user': user})


@login_required()
def update(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        first = request.POST.get('first')
        last = request.POST.get('last')
        username = request.POST.get('username')
        email = request.POST.get('email')
        user.first_name = first
        user.last_name = last
        user.username = username
        user.email = email
        user.save()
        return redirect('index')
    return render(request, 'users/register.html', {'user': user})
