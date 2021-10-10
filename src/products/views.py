from django.shortcuts import render
from django.views import View

from .models import Product


def ProductDetailView(request, id):
	pass

class ProductListView(View):
	template_name = 'products/product_list.html'
	queriset = Product.objects.all()

	def get_queriset(self):
		return self.queriset

	def get(self, request, *args, **kwargs):
		context = {'object_list': self.get_queriset()}
		return render(request, self.template_name, context)
