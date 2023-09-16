from django.views import generic

from product.models import Variant,Product,ProductVariant
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView

from product.forms import VariantForm
from product.models import Variant



class BaseVariantView(generic.View):

    model = Product
    template_name = 'products/create.html'
    success_url = '/product/list'
class ProductView(BaseVariantView, ListView):
    template_name = 'products/list.html'
    paginate_by = 4

    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return ProductVariant.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("sdfasfdddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")
        context['products'] = Product.objects.all()
        context['request'] = ''
        if self.request.GET:
            context['request'] = self.request.GET['title__icontains']
        return context
class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        product=Product.objects.all()
        context['product'] = list(product.all())
        context['variants'] = list(variants.all())
        return context
