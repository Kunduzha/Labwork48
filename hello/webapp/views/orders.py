from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from webapp.models import Order, GoodInCart, OrderGood


class Checkout(View):
    def post(self, request, *args, **kwargs):

        name = request.POST.get('name')
        adress = request.POST.get('adress')
        phomenumber = request.POST.get('phonenumber')
        order = Order.objects.create(name=name, adress=adress, phonenumber=phomenumber)
        if request.user.is_authenticated:
            order.user = request.user
            order.save()
        session = self.request.session.get('goods_in_cart', [])
        for cart in GoodInCart.objects.all().filter(pk__in=session):
            OrderGood.objects.create(order=order, good=cart.good, count=cart.count)
            cart.delete()
        request.session['goods_in_cart'] = []
        return redirect('main_page')




        #
        # checkout = get_object_or_404(Order, pk=kwargs.get('pk'))
        # if checkout.remainder > 0:
        #     try:
        #         good_cart = GoodInCart.objects.get(good=good)
        #         good_cart.count += 1
        #         checkout.save()
        #     except:
        #         GoodInCart.objects.create(good=good, count=1)
        #     good.remainder -= 1
        #     good.save()
        # return redirect('main_page')

    # def article_create_view(request):
    #
    #     if request.method == 'GET':
    #         return render(request, 'article_create.html')
    #     elif request.method == 'POST':
    #         context = {
    #             'name': request.POST.get('name'),
    #             'adress': request.POST.get('adress'),
    #             'Phomenumber': request.POST.get('phonenumber')
    #         }
    #         return render(request, 'article_view.html', context)

class CheckList(LoginRequiredMixin, ListView):
    context_key = 'checklist'
    model = Order
    template_name = 'Good/check_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return self.model.objects.filter(user__pk=self.request.user.id)

    def get_context_data(self,  object_list=None, **kwargs):

        context= super().get_context_data(object_list=object_list)
        print(self.request.user.id)
        print(context['orders'])
        total = 0
        for order in context['orders']:
            print(order.order_good.all())
            for order_goods in order.order_good.all():
                print(order_goods, '111111')
                total +=order_goods.get_total()
        context['total']=total
        return  context

    def get_objects(self):
        return super().get_objects()

