from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
#Views are Request handler, for a request send a response

# Create your views here.
def trial():
    x=1
    return x
def hello(request):
    x=trial()
    return render(request, 'hello.html', {'name' :'Gopika'})
