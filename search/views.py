from django.shortcuts import render
from .engine import engine
import json
# Create your views here.
app=engine()
def index(request):
    context={'a':'a'}
    obj=render(request,'search/index.html',context=context)
    return obj

def search(request):
    if 'q' in request.GET:
        keyword=request.GET['q']
        msg=app.search(keyword=keyword)
    else:
        msg = 'You submitted an empty form.'


    context={'message':msg,
             'keyword':keyword}
    obj=render(request,'search/result.html',context=context)
    return obj
