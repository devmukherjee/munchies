from . import views
from django.urls import path

app_name= 'food'
urlpatterns = [
    path('',views.index,name= "index"),
    path('<int:item_id>',views.details,name="detail"),
    path('items',views.items,name= "items"),
    
]