from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',Home,name='home'),
    path('blog/',Blog_list,name='blog_list')
]
