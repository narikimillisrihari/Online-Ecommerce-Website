from django.urls import path
from Products import views
urlpatterns = [
    path('create/',views.create , name='create'),
    path('sellerview/',views.sellerview , name='sellerview'),
    path('product_list/',views.product_list , name='product_list'),
    path('product_detail/<int:id>/',views.product_detail , name='product_detail'),
    
]
