from django.urls import path
from . import views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrderList.as_view(), name='orders_list'),
    path('forming/complete/<int:pk>/', ordersapp.order_forming_complete, name='order_forming_complete'),
    path('create/', ordersapp.OrderItemsCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', ordersapp.OrderRead.as_view(), name='order_read'),
    path('update/<int:pk>/', ordersapp.OrderItemsUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', ordersapp.OrderDelete.as_view(), name='order_delete'),
    path('product/<int:pk>/price/', ordersapp.get_order_price, name='product_price'),
]
