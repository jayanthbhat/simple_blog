from django.shortcuts import render
from .models import Posts
# Create your views here.
def home(request):
    post_query=Posts.objects.all()

    print(post_query[0].image)
    return render(request,'registration/home.html',context={'query_set':post_query})