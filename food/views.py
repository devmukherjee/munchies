from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
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

def create_item(request):
    form= ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context= {'form':form}
    return render(request,'food/item-form.html', context)
