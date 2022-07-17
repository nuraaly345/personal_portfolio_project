from django.shortcuts import render, get_object_or_404
from . models import Blog

def index(request):
    blogs = Blog.objects.order_by('-blog_time')[:5]

    return render(request, 'blog/index.html', {'blogs': blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
