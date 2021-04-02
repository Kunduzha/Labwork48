from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.urls import reverse_lazy

from webapp.models import Good
from webapp.forms import Goodform
from webapp.forms import Goodform
from webapp.forms import Goodform, GoodDeleteForm, SimpleSearchForm
from django.views.generic import View, TemplateView, RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode

# Create your views here.
class IndexView_good(ListView):
    model = Good
    template_name = 'Good/index.html'
    context_object_name = 'goods'
    paginate_by = 3
    paginate_orphans = 1


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, object_list = None, **kwargs):
        context = super().get_context_data(object_list= object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(name__icontains=self.search_value)  | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

# def main_page(request):
#     good=Good.objects.all().order_by('name', 'category')
#     return render(request, "Good/index.html", {'good': good})


#
# def good_more(request, pk):
#     good = get_object_or_404(Good, id=pk)
#     return render(request, "Good/good_more.html", {'good': good})

class Good_more(DetailView):
    model = Good
    template_name = 'Good/good_more.html'


# def good_add(request):
#     if request.method == "GET":
#         form = Goodform()
#         return render(request, 'Good/good_add.html', context={'form': form})
#     elif request.method == "POST":  # Если метод запроса POST - создаём статью и редиректим клиента
#         form = Goodform(data=request.POST)  # Создадим объект формы, в него передадим данные из формы, которые пришли от клиента
#         if form.is_valid():  # если форма валидна - создаётся статья и клиент редиректится
#             good = Good.objects.create(
#                 name=form.cleaned_data.get('name'),
#                 category=form.cleaned_data.get('category'),
#                 description=form.cleaned_data.get('description'),
#                 remainder=form.cleaned_data.get('remainder'),
#                 price=form.cleaned_data.get('price')
#             )
#             return redirect('see_good',
#                             pk=good.id)  # Перенаправляем клиента на страницуу детального просмотра статьи
#         return render(request, 'Good/good_add.html',
#                       context={'form': form})  # если форма не валидна - отобразим форму с ошибками


class Good_add(CreateView):
    template_name = 'Good/good_add.html'
    model = Good
    form_class = Goodform

    def get_success_url(self):
        return reverse('see_good', kwargs = {'pk': self.object.pk})



# def good_change(request, pk):
#     """
#     Представление для редактирования статьи
#     """
#     good = get_object_or_404(Good, id=pk)  # получаем статью
#
#     if request.method == 'GET':  # если метод запроса GET
#         form = Goodform(initial={  # создадим форму со стартоввыми данными полей, соответствующими данным полей статьи
#             'name': good.name,
#             'category': good.category,
#             'description': good.description,
#             'remainder': good.remainder,
#             'price': good.price
#
#         })
#         return render(request, 'Good/change_good.html', context={'form': form, 'good': good})  # и отобразим форму редактирования статьи
#     elif request.method == 'POST':  # Если метод запроса POST
#         form = Goodform(data=request.POST)  # Создадим объект формы, в него передадим данные из формы, которые пришли от клиента
#         if form.is_valid():
#             good.name = form.cleaned_data.get('name')
#             good.category = form.cleaned_data.get('category')
#             good.description = form.cleaned_data.get('description')
#             good.remainder = form.cleaned_data.get('remainder')
#             good.price = form.cleaned_data.get('price')
#             good.save()
#             return redirect('see_good', pk=good.id)  # после сохранения статьи перенаправим на страницу просмотра статьи
#
#         return render(request, 'Good/change_good.html', context={'form': form, 'good': good})  # если форма не валидна - отобразим форму с ошибками


class Good_change(UpdateView):
    model = Good
    template_name = 'Good/change_good.html'
    form_class = Goodform
    context_object_name = 'goods'

    def get_success_url(self):
        return reverse('see_good', kwargs={'pk': self.object.pk})


# def good_delete(request, pk):
#
#     good = get_object_or_404(Good, id=pk)  # получаем статью
#
#     if request.method == 'GET':  # если метод запроса GET - отобразим форму для подтверждения удаления статьи
#         form = GoodDeleteForm()
#         return render(request, 'Good/good_del.html', context={'good': good, 'form': form})
#     elif request.method == 'POST':  # если метод запроса POST - удалим статью и перенаправим на страницу списка статей
#         form = GoodDeleteForm(data=request.POST)
#         if form.is_valid():
#             if form.cleaned_data['name'] != good.name:
#                 form.errors['name'] = ['Названия товара не совпадают']
#                 return render(request, 'Good/good_del.html', context={'good': good, 'form': form})
#
#             good.delete()
#             return redirect('all_page')
#         return render(request, 'Good/good_del.html', context={'good': good, 'form': form})


class Good_delete(DeleteView):
    template_name = 'Good/good_del.html'
    model = Good
    context_object_name = 'goods'
    success_url = reverse_lazy('main_page')