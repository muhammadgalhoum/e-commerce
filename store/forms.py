from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
  desc = forms.CharField(widget=forms.Textarea(attrs={'rows': 5,'cols': 32}))
  
  class Meta:
    model = Product
    fields = '__all__'


class ProductDeleteForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = []   #Form has only submit button. Empty list still necessary.