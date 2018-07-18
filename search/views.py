from django.shortcuts import render

# Create your views here.
def index(request):
    context={'a':'a'}
    obj=render(request,'search/index.html',context=context)
    return obj

def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    context={'message':message}
    obj=render(request,'search/result.html',context=context)
    return obj
