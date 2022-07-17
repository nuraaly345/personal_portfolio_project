from django.shortcuts import render
from . models import Blog

def index(request):
    blogs = Blog.objects.order_by('-blog_time')[:5]

    return render(request, 'blog/index.html', {'blogs': blogs})
