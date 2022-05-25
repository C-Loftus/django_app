from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

data = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    }, 
    {
        'author': 'Bob Doe',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    }

]



def home(request):
    context = {
        'posts': data
    }
    return render(request, 'blog/home.html', context)
def about(request):
    return render(request, 'blog/about.html')