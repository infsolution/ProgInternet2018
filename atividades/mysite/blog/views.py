from django.shortcuts import render
from blog.models import *

def index(request):
    blog = Blog.objects.get(id=1)
    return render(request, 'blog/index.html',{'blog':blog})
