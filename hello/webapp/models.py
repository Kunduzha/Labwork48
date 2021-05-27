from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.
category_choice=[('new', 'новые'), ('old', 'просроченные')]


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract =  True


class Good(models.Model):
    name=models.CharField(max_length=100, null=False, blank=False, verbose_name="good_name")
    description=models.CharField(max_length=2000, null=True, blank=True, verbose_name='good_description')
    category=models.TextField(null=False, blank=False, choices=category_choice,  verbose_name='good_category')
    remainder=models.IntegerField(validators=[MinValueValidator(1)], null=False, blank=False, verbose_name='remainder' )
    price=models.DecimalField(validators=[MinValueValidator(0)], null=False, blank=False, max_digits=7, decimal_places=2)


    class Meta:
        db_table='goods'
        verbose_name='Good'
        verbose_name_plural='Goods'


    def __str__(self):
        return f'{self.id}. {self.name}:{self.remainder}'



class GoodInCart(models.Model):
     good = models.ForeignKey(
         'webapp.Good',
         on_delete=models.CASCADE,
         related_name='goods',
         verbose_name='Товары',
         null=False,
         blank=False
     )
     count = models.IntegerField(null= False, blank = False, validators = [MinValueValidator(0)])

     class Meta:
         verbose_name = 'Good'
         verbose_name_plural = 'Goods'

     def get_total(self):
         return self.count * self.good.price


# class Order(models.Model):
#
#     name = models.CharField(max_length=31, verbose_name='Тег')
#
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
#
#
#     def __str__(self):
#
#         return self.name



# class GoodinCartOrder(models.Model):
#
#     good = models.ForeignKey('webapp.Good', related_name='good_orders', on_delete=models.CASCADE, verbose_name='Статья')
#
#     order = models.ForeignKey('webapp.Order', related_name='order_goods', on_delete=models.CASCADE, verbose_name='Тег')
#
#
#     def __str__(self):
#
#         return "{} | {}".format(self.article, self.tag)

class OrderGood(models.Model):
    order = models.ForeignKey('webapp.Order', blank=False, null= False, on_delete=models.CASCADE, related_name='order_good')
    good = models.ForeignKey('webapp.Good', blank=False, null=False, on_delete=models.CASCADE)
    count = models.IntegerField(null=False, blank=False, verbose_name='количество')

    def get_total(self):
        return self.count * self.good.price




class Order(BaseModel):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Имя')
    phonenumber = models.CharField(max_length=20, null=False, blank=False, verbose_name='контакты')
    adress = models.CharField(max_length=50, null=False, blank=False, verbose_name='адрес')
    user = models.ForeignKey(User, blank=True, null=True, related_name='order', verbose_name='клиент', on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name} ({self.id})'

    def order_total(self):
        order_total=0
        for i in self.order_good.all():
            order_total+=i.get_total()
        return order_total