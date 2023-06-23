from . import views
from django.urls import path
#app name variable is used for namespacing gives us a manageable way to handle namespaces for url patterns
app_name= 'food'
urlpatterns = [
    path('',views.index,name= "index"),
    path('<int:item_id>',views.details,name="detail"),
    path('items',views.items,name= "items"),
    # add item to the databse
    path('add',views.create_item,name="create_item"),
    
]