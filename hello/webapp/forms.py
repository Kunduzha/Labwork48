from django import forms
from webapp.models import Good


class Goodform(forms.ModelForm):
    class Meta:
        model=Good
        fields=('name', 'description', 'category', 'remainder', 'price')

class GoodDeleteForm(forms.Form):
    name=forms.CharField(max_length=100, required=True, label='Введите название товара чтобы удалить его')


