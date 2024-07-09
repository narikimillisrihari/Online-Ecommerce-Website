from django.forms import ModelForm
from Products.models import CreateProduct

class CreateProductForm(ModelForm):
    class Meta:
        model=CreateProduct
        fields="__all__"