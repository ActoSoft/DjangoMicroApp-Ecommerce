from django.urls import path
from .views import GetProducts

app_name = 'products'
urlpatterns = [
    path('', GetProducts.as_view(), name='list')
]