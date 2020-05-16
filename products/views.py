from django.shortcuts import render
from django import views
from django.db.models import Q
from .models import Product

class GetProducts(views.View):
    def get(self, request):
        # if request.GET.get('search') and request.GET.get('category'):
        #     print("llego")
        #     value = request.GET['search']
        #     category = request.GET['category']
        #     products = Product.objects.filter(
        #         Q(name__icontains=value),
        #         category=category,
        #         is_active=True
        #     )
        # else:
        #     print("NO llego")
        #     products = Product.objects.filter(is_active=True)
        # products = Product.objects.all()
        # print("P1", products)
        # products = products.filter(is_active=True)
        # print("P2", products)
        products = Product.objects.filter(is_active=True)
        if request.GET.get('search'):
            search = request.GET['search']
            products = products.filter(Q(name__icontains=search))
        if request.GET.get('category'):
            category = request.GET['category']
            products = products.filter(category=category)
        counter = len(products)
        template_name = 'products/list.html'
        context = {
            'products': products,
            'counter': counter
        }
        return render(request, template_name, context)
