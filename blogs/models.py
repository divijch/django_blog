from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        
    def __str__ (self):
        return self.category_name
    
STATUS_CHOICES = (
    ("Draft",'Draft'),
    ("Published",'Published'),   
)
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d' )
    short_description = models.TextField(max_length=500)
    blog_body = models.TextField(max_length=5000)
    status = models.CharField(choices=STATUS_CHOICES, default="draft", max_length=20)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.title
    
class About(models.Model):
    about_Heading = models.CharField(max_length=50)
    about_description = models.TextField(max_length=500)
    
    def __str__ (self):
        return self.about_Heading
    
class Social(models.Model):
    social_title = models.CharField(max_length=50)
    social_link = models.URLField(max_length=500)
    def __str__ (self):
        return self.social_title
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment