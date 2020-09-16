from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, UserProfileUpdateForm, ProfilePic
# Create your views here.


def sign_up(request):
    form = SignupForm()
    registered = False
    if request.method == 'POST':
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    context = {'form': form, 'registered': registered, }
    return render(request, 'App_Login/signup.html', context=context)


def user_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=user_name, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    context = {'form': form}
    return render(request, 'App_Login/login.html', context=context)


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def profile(request):
    context = {}
    return render(request, 'App_Login/profile.html', context=context)


@login_required
def update_profile(request):
    current_user = request.user
    form = UserProfileUpdateForm(instance=current_user)
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileUpdateForm(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    context = {'form': form}
    return render(request, 'App_Login/update_profile.html', context=context)


@login_required
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
    context = {'form': form, 'changed': changed}
    return render(request, 'App_Login/change_password.html', context=context)


@login_required
def add_pro_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    context = {'form': form}
    return render(request, 'App_Login/add_pro_pic.html', context=context)


@login_required
def change_pro_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    context = {'form': form}
    return render(request, 'App_Login/add_pro_pic.html', context=context)