from django.shortcuts import render, redirect, get_object_or_404
from .models import Recommend_Post, Subscribe_Cart
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request):
    return render(request, 'detail.html')

def postlist(request):
    return render(request, 'postlist.html')

#구독 바구니에서 회원이 user와 같다면 get.
def mypage(request):
    myposts = Recommend_Post.objects
    search = request.GET.get('search')
    if search == 'true':
        writer = request.GET.get('writer')
        myposts = Recommend_Post.objects.filter(author = writer)
        # mysubcribe_posts = Subscribe_Cart.objects.filter(user = writer)
        # ,{'mysubcribe_posts':mysubcribe_posts})  
    return render(request, 'mypage.html',{'myposts':myposts})

def making(request):
    return render(request, 'making.html')

