from django.shortcuts import render
from django.http import HttpResponse
# .models means models.py of current package
from .models import Posts

# Basic structure of the views.py, passing direct html code
# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Reached blog home page</h1>")
# def about(request):
#     return HttpResponse("<h1>About Blog</h1>")

# Dummy data to display on the web pages
# Dummy data replaced by the data from Posts model
context = {
    "posts" : [
    {
        "author":"The Django guru ",
        "Title" : "Django template engine",
        "Text"  : """
        Being a web framework, Django needs a convenient way to generate HTML 
        dynamically. The most common approach relies on templates. A template 
        contains the static parts of the desired HTML output as well as some 
        special syntax describing how dynamic content will be inserted.
        
        A Django project can be configured with one or several template engines
        (or even zero if you don’t use templates). Django ships built-in 
        backends for its own template system, creatively called the Django 
        template language (DTL), and for the popular alternative Jinja2. 
        Backends for other template languages may be available from 
        third-parties.   
                """,
        "Created" : "Jan 06, 2020"
    },
    {
        "author": "w3school",
        "Title" : "What's Bootstrap",
        "Text"  : """
        Bootstrap is the most popular CSS Framework for developing responsive 
        and mobile-first websites. Bootstrap 4 is the newest version of 
        Bootstrap
        """,
        "Created" : "Jan 06, 2020"
    }
        ]
}

# Using django render to render html templates
# Passing context as the third argument to the render method. Content of
# context is made available in the .html template where it can be used in the
# Django Template Language code


def home(request):
    db_context = {
        "posts": Posts.objects.all()
    }
    return render(request, 'blog/home.html', db_context)


def about(request):
    return render(request, 'blog/about.html')
