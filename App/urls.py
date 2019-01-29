from django.urls import path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('home/', Home, name="home"),
    path('login/', Login, name="login"),
    path('singup/', Singup, name="singup"),
    path('profile/', Profile, name="profile"),
    path('logout/', Logout, name="logout"),
]