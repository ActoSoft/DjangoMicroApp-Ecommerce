from django.urls import path
from .views import GetProducts, GetProduct

app_name = 'products'
urlpatterns = [
    path('', GetProducts.as_view(), name='list'),
    path('<int:id>', GetProduct, name='detail')
]