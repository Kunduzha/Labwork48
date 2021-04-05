from django.shortcuts import get_object_or_404, redirect
from django.views import View

from webapp.models import Order, GoodInCart, OrderGood


class Checkout(View):
    def post(self, request, *args, **kwargs):
        print("dsxs")
        name = request.POST.get('name')
        adress = request.POST.get('adress')
        phomenumber = request.POST.get('phonenumber')
        order = Order.objects.create(name=name, adress=adress, phonenumber=phomenumber)

        for cart in GoodInCart.objects.all():
            OrderGood.objects.create(order=order, good=cart.good, count=cart.count)
            cart.delete()
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

