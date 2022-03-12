from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include


def all1(request):

    return render(request, "index.html")

def Profile(request):
    return render(request, 'profile.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', all1),
    path('accounts/profile/', Profile),
]

admin.site.site_header = 'ALEVcoder admin'