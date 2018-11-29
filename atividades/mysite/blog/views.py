from django.shortcuts import render, redirect
from blog.models import *
from blog.forms import PostForm
def index(request):
    #blog = Blog.objects.get(id=1)
    #return render(request, 'blog/index.html',{'blog':blog})
	posts = Post.objects.order_by('-data_published').reverse()
	return render(request,'blog/index.html', {'posts':posts})

def add_post(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.save()
			return redirect('index')
	else:
		form = PostForm()
	return render(request, "blog/add_post.html", {'form': form})	