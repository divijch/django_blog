from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from blogs.models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # Fetch the posts the belongs to the category with the category_id
    posts = Blog.objects.filter(status="Published", category=category_id)
   # try:
       #category = Category.objects.get(pk=category_id)
    #except:
       # return redirect('home')
    #use try and except to redrirect to home or do something or use get object or 404 for 404 page
    
    category = get_object_or_404(Category,  pk=category_id) 
    
    context = {
        'posts': posts,
        'category': category,
    } 
    return render(request, 'posts_by_category.html', context)

def blogs (request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status="Published")
    context ={
        'single_blog': single_blog
    }
    return render (request, 'blogs.html', context)