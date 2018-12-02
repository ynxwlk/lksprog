#from django.http import HttpResponse    #first
from django.shortcuts import render
 
def hello(request):
    # return HttpResponse("Hello world ! ") #first
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)