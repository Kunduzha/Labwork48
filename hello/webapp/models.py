from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
category_choice=[('new', 'новые'), ('old', 'просроченные')]
class Good(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False, verbose_name="good_name")
    description=models.CharField(max_length=2000, null=True, blank=True, verbose_name='good_description')
    category=models.TextField(null=False, blank=False, verbose_name='good_category')
    remainder=models.IntegerField(validators=[MinValueValidator(0)], null=False, blank=False, verbose_name='remainder' )
    price=models.DecimalField(null=False, blank=False, max_digits=7, decimal_places=2)


    class Meta:
        db_table='goods'
        verbose_name='Good'
        verbose_name_plural='Goods'


    def __str__(self):
        return f'{self.id}. {self.name}:{self.remainder}'