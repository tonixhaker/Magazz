from django import forms
from .models import *

class OwnDateField(forms.DateInput):
    input_type = 'date'

class ProductForm(forms.ModelForm):
    # published = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['count']
        widgets = {
            'publishdate': OwnDateField()
        }

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['descript'].widget.attrs.update({'class': 'form-control'})
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['publishdate'].widget.attrs.update({'class': 'form-control'})


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        exclude = ['count']

    def __init__(self, *args, **kwargs):
        super(CategoriesForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = {'quantity','product'}

    def __init__(self, *args, **kwargs):
        super(CartForm, self).__init__(*args, **kwargs)
        self.fields['quantity'].widget.attrs.update({'class' : 'form-control'})
        self.fields['product'].widget.attrs.update({'class': 'form-control'})