from django.shortcuts import render
from .models import Posts
from phadke_app.forms import AddPostsForm
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def home(request):
    post_query=Posts.objects.all()[:3]

    print(post_query[0].image)
    return render(request,'registration/home.html',context={'query_set':post_query})

def list_posts(request):
    post_query=Posts.objects.all()
    return render(request,'registration/posts/list_posts.html',context={'query_set':post_query})

def view_post(request,pk):
    data_query = get_object_or_404(Posts,pk=pk)
    print(data_query)
    return render(request,'registration/posts/view_post.html',context={'data_query':data_query})

def add_posts(request):
    if request.method == "POST":  
        form = AddPostsForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()
    else:  
        form = AddPostsForm()  
    return render(request,'registration/posts/add_posts.html',context={'form':form})


    
    