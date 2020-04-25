
from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home, name='home'),
    path('products', views.products, name='products'),
    path('customers/<str:pk>/', views.customers, name='customers'),
    path('products', views.products, name='products'),
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>', views.update_order, name='update_order'),
    path('delete/<str:pk>', views.delete, name='delete'),
]
