from django.shortcuts import render
from blogs.models import Category, Blogs

# Create your views here.
def home_view(request):
    categories=Category.objects.all()
    featured_blogs=Blogs.objects.filter(is_featured=True)
    posts=Blogs.objects.filter(is_featured=False, status='public')
    context={
        'categories':categories,
        'featured_blogs':featured_blogs,
        'posts':posts

    }
    return render(request, 'home.html', context)
