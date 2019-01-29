from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.urls import reverse
from .models import Entry
User = get_user_model()


def Reverse(url, args=()):
    return HttpResponseRedirect(reverse(url, args))


def Home(request):

    context = {"User": request.user}
    return render(request, "Home.html", context=context)

def Singup(request):
    if not request.user. is_authenticated:
        if request.method == "GET":
            return render(request, "Singup.html")

        if request.method == "POST":
            User = get_user_model()
            uname = request.POST['Username']
            email = request.POST['Email']
            pass1 = request.POST['Password1']
            pass2 = request.POST['Password2']
            if uname and email and pass1 and pass2 and pass1 == pass2:
                user = User.objects.create_user(username=uname, email=email, password=pass1)
                user.is_active = True
                return HttpResponse("OK Done")
            else:
                return HttpResponseRedirect(reverse('singup'))
    else:
        return HttpResponseRedirect(reverse('profile'))

def Login(request):
    if request.method == "GET":
        return render(request,"Login.html")

    if request.method == "POST":
        username = request.POST['Username']
        password = request.POST['Password']
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
            else:
                print('---')
                print(user)
                print('---')
                return render(request, "Login.html")

def Profile(request):
    user = request.user
    if user.is_authenticated:
        ents = user.entry.all()
        context = {'ents': ents}
        if request.method == "GET":
            ents = User.objects.get(username=request.user)
            ents = ents.entry.all()
            context = {'ents': ents}
            return render(request, "Profile.html", context=context)

        if request.method == "POST":
            entry = request.POST['Entry']
            user = User.objects.get(username=user)
            if entry:
                e = Entry(user=user, entry=entry)
                e.save()
                return render(request, "Profile.html",context=context)
            else:
                return render(request, "Profile.html",context=context)
    else:
        return Reverse('login') #here i use helper function



@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
