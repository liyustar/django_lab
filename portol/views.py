from django.shortcuts import render

from django.http import HttpResponse
import datetime

def hello_world(request):
    return render(request, 'hello.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    my_context = {
        "my_text": "This is about us.",
        "my_num": 123,
    }
    return render(request, 'about.html', my_context)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)