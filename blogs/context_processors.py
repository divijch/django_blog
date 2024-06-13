from . models import Category,About,Social

def get_categories(request):
    categories = Category.objects.all()
    about = About.objects.all()
    social = Social.objects.all()
    return dict(categories=categories, about=about, social=social)