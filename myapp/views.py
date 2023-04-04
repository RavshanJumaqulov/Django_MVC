from django.shortcuts import render
from myapp.models import *
# Create your views here.


def Home(request):
    return render(request,'myapp/home.html')



def Blog_list(request):
    blogs = Blog.objects.all()
    return render(request,'myapp/blog_list.html',{"blogs":blogs})