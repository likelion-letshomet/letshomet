from django.db import models
from django.shortcuts import render, redirect, get_object_or_404
import getpass
from .models import Recommend_Post, Subscribe_Cart
from django.core.paginator import Paginator
from django.utils import timezone


# Create your views here.

def home(request):
    return render(request, 'home.html')

def detail(request,id):
    post = get_object_or_404(Recommend_Post,pk=id)
    return render(request, 'detail.html', {'post':post})

def postlist(request):
    posts = Recommend_Post.objects.all()
    return render(request, 'postlist.html', {'posts':posts})



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
def create(request):
    new_post = Recommend_Post()
    new_post.title = request.POST['title']
    new_post.author = request.POST['author']
    new_post.context = request.POST['context']
    new_post.created_date = timezone.now()
    #post_url
    new_post.post_url1 = request.POST['post_url1']
    new_post.post_url2 = request.POST['post_url2']
    new_post.post_url3 = request.POST['post_url3']
    new_post.save()
    return redirect('home')
