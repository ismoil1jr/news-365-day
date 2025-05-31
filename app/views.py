from django.shortcuts import render,redirect
from .models import Blog, Category, Tag, Comment
from user.models import Author
from django.contrib.auth.decorators import login_required
from utils.views import group_queryset
from django.core.paginator import Paginator

def index(request):
    
    header = Blog.objects.order_by('-id')[:5]
    resent_new = Category.custom.filter(translations__name__in = ['politics','technology']).distinct()
    blogs = Blog.objects.all()
    business = Category.custom.get_category('business')
    sport = Category.custom.get_category('sport')
    gadgets = Category.custom.get_category('gadgets')
    life_style = Category.custom.get_category('life-style')
    travel = Category.custom.get_category('travel')
    author = Author.objects.all()

    gadgets_blogs = Blog.objects.filter(category = gadgets)

    gadgets_paginator = Paginator(gadgets_blogs,5)
    page_number = request.GET.get("page",1)
    gadgets_by_page = gadgets_paginator.get_page(page_number)




    context = {
        'resent_new':resent_new,
        'header': header,
        'blogs': group_queryset(2,blogs),
        'business': business,
        'sport': sport,
        'gadgets':  gadgets,
        "gadgets_by_page":gadgets_by_page,
        'life_style': life_style,
        'travel': travel,
        'author':author,
    }
    return render(request, 'index.html', context)



def blog_detail(request, id):
    blog = Blog.objects.get(id=id)
    comments = Comment.objects.filter(blog=blog).order_by('-time')
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            text = request.POST.get('text')
            if text:
                Comment.objects.create(blog=blog, user=request.user, text=text)
                return redirect('blog_detail', id=id)
    
    related_blogs = Blog.objects.filter(category=blog.category).exclude(id=blog.id)

    context = {
        'blog': blog,
        'comments': comments,
        'related_blogs': related_blogs,
    }
    return render(request, 'blog_single.html', context)



def base(request):
    
    header = Blog.objects.order_by('-id')[:5]
    resent_new = Category.custom.filter(name__in = ['Politics','Technology'])
    blogs = Blog.objects.all()
    business = Category.custom.get_category('Business')
    sport = Category.custom.get_category('Sport')
    gadgets = Category.custom.get_category('Gadgets')
    life_style = Category.custom.get_category('Life Style')
    travel = Category.custom.get_category('Travel')

    context = {
        'resent_new':resent_new,
        'header': header,
        'blogs': group_queryset(2,blogs),
        'business': business,
        'sport': sport,
        'gadgets': gadgets,
        'life_style': life_style,
        'travel': travel,
        
    }
    return render(request, 'base.html',context)


def page_404(request):

    blogs = Blog.objects.all()
    
    context = {
        'blogs': blogs,
        
    }
    return render(request, '404.html',context)



def authors(request):
    
    authors = Author.objects.all()
    business = Category.custom.get_category('business')

    context = {
        'author': authors,
        'business':business
        

    }     
    return render(request, 'author.html',context)



def blog_single(request):
    blog = Blog.objects.all()
    comments = Comment.objects.filter(blog=blog).order_by('-time')
    

    context = {
        'blog': blog,
        'comments': comments,
         
     }
    return render(request, 'blog_single.html',context)



def blog(request):
    blogs = Blog.objects.all()
    author = Author.objects.first()
    category = Category.custom.all()
    comments = Comment.objects.all()
    sport = Category.custom.get_category('sport')
    business = Category.custom.get_category('business')
    title = request.GET.get("title")

    if title:
        blogs = blogs.filter(translations__title__icontains = title)



    context = {
        'author':author,     
        'blogs': blogs,      
        'comments': comments,
        'category': category,
        'title':title,        
        'sport': sport,
        'business': business,
    }

    return render(request, 'blog.html',context)



def contact(request):
    

    context = {
        

    }
    return render(request, 'contact.html',context)



def gallery_single(request):
    

    context = {
        

    }
    return render(request, 'gallery_single.html',context)



def gallery(request):
    
    resent_new = Blog.objects.all()
    context = {
        
        'resent_new':resent_new,

    }
    return render(request, 'gallery.html',context)



def life_style(request):
    
    life_style = Category.custom.get_category('life-style')
    sport = Category.custom.get_category('sport')
    business = Category.custom.get_category('business')
    blogs = Blog.objects.all()[:1] 
    context = {
        'life_style' : life_style,
        'sport'      : sport,
        'business'   : business,
        'blogs'      : blogs
    }

    return render(request, 'life_style.html',context)



def sport(request):
    
    sport = Category.custom.get_category('sport')

    context = {
        'sport':sport,
        
    }

    return render(request, 'sport.html',context)



def technology(request):
    
    gadgets = Category.custom.get_category('gadgets')

    context = {
        'gadgets': gadgets,
        
    }

    return render(request, 'technology.html',context)



@login_required
def profile(request):
    if request.method == 'POST':
        new_username = request.POST.get('username')
        if new_username:
            request.user.username = new_username
            request.user.save()
            return redirect('profile')
    
    liked_blogs = Blog.objects.filter(like__user=request.user)
    user_comments = Comment.objects.filter(user=request.user)
    context = {
        'liked_blogs': liked_blogs,
        'user_comments': user_comments
    }

    return render(request, 'profile.html',context)


