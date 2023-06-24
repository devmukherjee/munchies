from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView 

# COnverted above function based view into class based viewiew
#from django.template import loader
# Create your views here.


# def index(request):
#     item_list= Item.objects.all()
#     #template= loader.get_template('food/index.html')
#     context={'item_list':item_list}
#     #return HttpResponse(template.render(context,request))
#     """
#     USing render function is more effecient than loader and Httpresponse
#     """
#     return render(request,'food/index.html',context)
# COnverted above function based view into class based view
class IndexClassView(ListView):
    model= Item
    template_name='food/index.html'
    context_object_name='item_list'

def items(request):
    #this is a random view just for testing
    return HttpResponse("<h1>This is an Item View</h1><br><p>This Page shows a list of items</p>")

# def details(request,item_id):
#     item= Item.objects.get(pk= item_id)
#     context= {'item':item}
#     return render(request,'food/details.html',context)
# COnverted above function based view into class based view
class FoodDetail(DetailView):
    model= Item
    template_name= 'food/details.html'
    #context_object_name= 'item'

# def create_item(request):
#     form= ItemForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         return redirect('food:index')

#     context= {'form':form}
#     return render(request,'food/item-form.html', context)
# COnverted above function based view into class based view

class CreateItemView(CreateView):
    model= Item
    fields=['item_name','item_desc','item_price','item_image']
    template_name= 'food/item-form.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user_name= self.request.user
        return super().form_valid(form)



def update_item(request,id):
    item= Item.objects.get(id= id)
    form= ItemForm(request.POST or None, instance= item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context= {'form':form, item: item}
    return render(request,'food/item-form.html', context)

def delete_item(request,id):
    item= Item.objects.get(id= id)

    if request.method =="POST":
        item.delete()
        return redirect('food:index')
    
    context= {"item": item}
    return render(request,'food/item-delete.html',context)

