from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'detail.html')

def mypage(request):
    return render(request, 'mypage.html')

def making(request):
    return render(request, 'making.html')

