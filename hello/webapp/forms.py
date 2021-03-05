from webapp.models import Good


class Goodform(forms.ModelForm):
    class Meta:
        model=Good
        feelds=('name', 'description', 'category', 'remainder', 'price')

class GoodDeleteForm(forms.form):
    name=forms.CharField(maxlength=100, required=True, label='Введите название товара чтобы удалить его')


