from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
#from django.template import loader
# Create your views here.

def index(request):
    item_list= Item.objects.all()
    #template= loader.get_template('food/index.html')
    context={'item_list':item_list}
    #return HttpResponse(template.render(context,request))
    """
    USing render function is more effecient than loader and Httpresponse
    """
    return render(request,'food/index.html',context)

def items(request):
    #this is a random view just for testing
    return HttpResponse("<h1>This is an Item View</h1><br><p>This Page shows a list of items</p>")

def details(request,item_id):
    item= Item.objects.get(pk= item_id)
    context= {'item':item}
    return render(request,'food/details.html',context)
