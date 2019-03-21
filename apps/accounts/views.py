from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required

from apps.accounts.models import UserAccount


# Create your views here.
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            message = "Authenticate failed. Please check username or password!"
            return render(request, 'login.html', {"message": message})
        pass
    elif request.method == "GET":
        return render(request, 'login.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username', "")
        email = request.POST.get('email', "")
        password = request.POST.get('password', "")
        password = make_password(password)
        if UserAccount.objects.filter(username=username):
            return render(request, 'register.html', {"message": "User has already existed"})
        user = UserAccount.objects.create(username=username, email=email, password=password)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return HttpResponseRedirect('/')
    elif request.method == "GET":
        return render(request, 'register.html')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')


def about(request):
    return render(request, 'about.html')


@login_required
def account(request):
    return render(request, 'account.html')


@login_required
def change_account(request):
    return render(request, 'account_update.html')


@login_required
def change_password(request):
    user = request.user
    old_password = request.POST.get('oldPassword')
    password = request.POST.get('newPassword')
    re_password = request.POST.get('rePassword')
    if password != re_password:
        msg = 'Please Confirm Your Password! password is different'
        return render(request, 'account_update.html', {'msg': msg})
    if check_password(old_password, user.password):
        user.password = make_password(password)
        user.save()
        return HttpResponseRedirect('/login')
    else:
        msg = 'Old password is wrong!'
        return render(request, 'account_update.html', {'msg': msg})


@login_required
def change_username(request):
    user = request.user
    username = request.POST.get('username')
    user_existed = UserAccount.objects.filter(username=username).first()
    if user_existed is not None:
        msg = 'username ' + username + 'already exists'
        return render(request, 'account_update.html', {'msg': msg})
    else:
        user.username = username
        user.save()
        return HttpResponseRedirect('/change_account')


@login_required
def change_mugshot(request):
    file = request.FILES.get('userPhoto')
    user = request.user
    user.mugshot = file
    user.save()
    print(user.mugshot)
    return HttpResponseRedirect('/change_account')
