from django.contrib import admin
from . models import Category, Blog, Social, About, User

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display=('title','category','author', 'status', 'is_featured')
    search_fields = ('id', 'title','category__category_name','status')
    list_editable= ('is_featured', 'status')

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Social)
admin.site.register(About)