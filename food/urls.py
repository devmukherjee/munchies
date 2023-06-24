from . import views
from django.urls import path
#app name variable is used for namespacing gives us a manageable way to handle namespaces for url patterns
app_name= 'food'
urlpatterns = [
    path('',views.IndexClassView.as_view(),name= "index"),
    path('<int:pk>',views.FoodDetail.as_view(),name="detail"),
    path('items',views.items,name= "items"),
    # add item to the databse
    path('add',views.CreateItemView.as_view(),name="create_item"),
    path('update/<int:id>/',views.update_item, name= "update_item"),
    path('delete/<int:id>/',views.delete_item,name="delete_item"),
    
]