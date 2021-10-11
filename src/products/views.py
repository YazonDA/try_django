from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import (
		ListView,
		DetailView
	)

from .models import Product


class ProductDetailView(DetailView):
        template_name = 'products/product_detail.html'
        # queryset = Article.objects.all()
        # queryset = Article.objects.filter(id__gt=1)

        def get_object(self):
                id_ = self.kwargs.get('id')
                return get_object_or_404(Product, id=id_)

class ProductListView(View):
	template_name = 'products/product_list.html'
	queriset = Product.objects.all()

	def get_queriset(self):
		return self.queriset

	def get(self, request, *args, **kwargs):
		context = {'object_list': self.get_queriset()}
		return render(request, self.template_name, context)

# class ProductListView(ListView):
# 	template_name = 'products/product_list.html'
# 	queriset = Product.objects.all()
