from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Div, Fieldset, HTML
from django import forms
from django.forms import inlineformset_factory

from apps.helpers.custom_layout_object import Formset
from apps.product.models import ProductImage, Product


class ProductImgForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', ]


ProductFormSet = inlineformset_factory(
    Product, ProductImage, form=ProductImgForm,
    fields=['image', ],
    extra=1
)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'category', 'brand', 'tag', 'color', 'size', 'thumbnail', 'price', 'is_offer', 'offer_price',
                  'short_description', 'long_description')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for fieldname in self.fields:
            self.fields[fieldname].help_text = None

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('category', css_class='form-group col-md-3 mb-0'),
                Column('brand', css_class='form-group col-md-3 mb-0'),
                Column('tag', css_class='form-group col-md-4 mb-0'),
                Column('color', css_class='form-group col-md-4 mb-0'),
                Column('size', css_class='form-group col-md-4 mb-0'),
                Column('thumbnail', css_class='form-group col-md-12 mb-0'),
                Column('price', css_class='form-group col-md-4 mb-0'),
                Column('is_offer', css_class='form-group col-md-4 mb-0'),
                Column('offer_price', css_class='form-group col-md-4 mb-0'),
                Column('short_description', css_class='form-group col-md-12 mb-0'),
                Column('long_description', css_class='form-group col-md-12 mb-0'),
            ),
            Div(
                Row(
                    Column(
                        Fieldset('Product Images:', Formset('formset'))
                    )
                ),
                css_class='col custom-col'
            ),
            Row(
                Column(
                    Submit('submit', 'Save')
                ),
            )
        )
