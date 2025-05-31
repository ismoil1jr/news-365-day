from django.urls import path
from .views import (
    index,
    page_404,
    authors,
    blog_single,
    blog,
    contact,
    gallery_single,
    gallery,
    life_style,
    sport,
    technology,
    blog_detail,
    profile
    
    
)

urlpatterns = [
    path('', index, name='home'),
    path('404/', page_404, name='page_404'),
    path('author/', authors, name='author'),
    path('blog_single/', blog_single, name='blog_single'),
    path('blog/', blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('gallery_single/', gallery_single, name='gallery_single'),
    path('gallery/', gallery, name='gallery'),
    path('life_style/', life_style, name='life_style'),
    path('sport/', sport, name='sport'),
    path('technology/', technology, name='technology'),
    path('blog/<int:id>/', blog_detail, name='blog_detail'),
    path('profile/', profile, name='profile'),
    
]
# This code defines the URL patterns for a Django application. Each URL pattern is associated with a specific view function that handles requests to that URL. The urlpatterns list contains all the defined URL patterns, and each pattern is created using the path() function, which takes the URL path, the view function, and an optional name for the URL pattern.




