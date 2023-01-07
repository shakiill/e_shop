from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.product.forms import ProductForm, ProductFormSet
from apps.product.models import Product


# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'product/list.html'


class ProductAddView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'add.html'
    success_url = reverse_lazy('product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ProductFormSet(self.request.POST, self.request.FILES)
        else:
            context['formset'] = ProductFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()
                return super().form_valid(form)
            else:
                return self.render_to_response(context)
