from django.shortcuts import render
from django.views import View

from products.models import Product


class ShopListView(View):
	template_name = 'shop_list/shop_list.html'
	# queriset = ShopList.objects.all()
	queriset = Product.objects.all()

	def get_queriset(self):
		return self.queriset

	def get(self, request, *args, **kwargs):
		context = {'object_list': self.get_queriset()}
		return render(request, self.template_name, context)
