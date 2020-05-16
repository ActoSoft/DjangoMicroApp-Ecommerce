from django.shortcuts import render
from django import views
from django.db.models import Q
from .models import Product

class GetProducts(views.View):
    def get(self, request):
        products = Product.objects.filter(is_active=True)
        search = request.GET['search'] if request.GET.get('search') else None
        category = request.GET['category'] if request.GET.get('category') else None
        if search:
            products = products.filter(Q(name__icontains=search))
        if category:
            products = products.filter(category=category)
        counter = len(products)
        template_name = 'products/list.html'
        context = {
            'products': products,
            'counter': counter,
            'search': search,
            'category': category
        }
        return render(request, template_name, context)

def GetProduct(request, id):
    product = Product.objects.get(pk=id, is_active=True)
    template_name = 'products/detail.html'
    context = {
        'product': product
    }
    return render(request, template_name, context)
