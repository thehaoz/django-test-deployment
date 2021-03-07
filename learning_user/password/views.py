from django.shortcuts import render
from password.forms import UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    return render(request, 'password_app/index.html')

def registration(request):

    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() ### SAVING THE USER FORM IN TO THE Database
            user.set_password(user.password) ### PROVIDE HASHING FOR THE PASSWORD OF THE USER
            user.save() ### SAVE THE HASH VERSION OF PASSWORD IN THE DATABASE

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pics' in request.FILES:
                profile.profile_pic = request.FILES['profile_pics']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm
    return render(request,
                    'password_app/registration.html',
                     {'user_form': user_form,
                     'profile_form': profile_form,
                     'registered': registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,
                            password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('password_app:index'))
            else:
                return HttpResponse("Account not active")
        else:
            print("someone tried to login and failed")
            print("username: {} and password {} ".format(username, password))
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'password_app/user_login.html')

@login_required
def special(request):
    return HttpResponse("You are logged in")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('password_app:index'))
