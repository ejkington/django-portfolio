from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'base/home.html')


def my_view(request):
    response = HttpResponse(open('/path/to/your/css/file.css', 'r').read())
    response['Content-Type'] = 'text/css'
    return response
