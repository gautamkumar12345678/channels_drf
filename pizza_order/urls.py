from django.urls import path
from .views import *

urlpatterns = [
    path('', PizzaAdminView.as_view({'get': 'list', 'post': 'create'})),
    path('product_view/<int:pk>', PizzaAdminView.as_view({'delete': 'destroy', 'patch': 'partial_update'})),
    path('view_product/', PizzaAllView.as_view({'get': 'list'})),
    path('address/', AddressView.as_view({'get': 'list'})),
    path('address_write/<int:pk>', AddressWrite.as_view({'delete': 'destroy', 'patch': 'partial_update'})),
    path('address_create/', AddressCreate.as_view({'post': 'create'})),
    path('cart/', CartView.as_view({'post': 'create', 'get': 'list'})),
    path('cartpizza/<int:pk>', CartPizzaView.as_view({'patch': 'partial_update', 'delete': 'destroy'})),
    path('cartpizza/', CartPizzaView.as_view({'get': 'list'})),
    path('order/', OrderCreate.as_view({'post': 'create', 'get': 'list'})),
    path('login/', login_request, name='login'),
    path('home/order_status/<str:order_idd>', order_status, name='order_status'),
    path('home/', home, name='home')
]
