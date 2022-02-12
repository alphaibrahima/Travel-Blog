from django.shortcuts import render
from .models import Post

# Create your views here.




def index(request):
    postlist = Post.objects.all()
    return render(request, 'main/index.html', {'postlist' :postlist})

def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist' :postlist})

def postdetails(request, pk):
    postlist = Post.objects.get(pk=pk)
    return render(request, 'main/postdetails.html', {'postlist' : postlist})