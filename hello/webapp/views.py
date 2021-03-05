from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Good
from webapp.forms import Goodform
from webapp.forms import Goodform
from webapp.forms import Goodform, GoodDeleteForm

# Create your views here.
def main_page(request):
    good=Good.objects.all().order_by('name', 'category')
    return render(request, "main.html", {'good': good})



def good_more(request, pk):
    good = get_object_or_404(Good, id=pk)
    return render(request, "good_more.html", {'good': good})



def good_add(request):
    if request.method == "GET":
        form = Goodform()
        return render(request, 'good_add.html', context={'form': form})
    elif request.method == "POST":  # Если метод запроса POST - создаём статью и редиректим клиента
        form = Goodform(data=request.POST)  # Создадим объект формы, в него передадим данные из формы, которые пришли от клиента
        if form.is_valid():  # если форма валидна - создаётся статья и клиент редиректится
            good = Good.objects.create(
                name=form.cleaned_data.get('name'),
                category=form.cleaned_data.get('category'),
                description=form.cleaned_data.get('description'),
                remainder=form.cleaned_data.get('remainder'),
                price=form.cleaned_data.get('price')
            )
            return redirect('see_good',
                            pk=good.id)  # Перенаправляем клиента на страницуу детального просмотра статьи
        return render(request, 'good_add.html',
                      context={'form': form})  # если форма не валидна - отобразим форму с ошибками






def good_change(request, pk):
    """
    Представление для редактирования статьи
    """
    good = get_object_or_404(Good, id=pk)  # получаем статью

    if request.method == 'GET':  # если метод запроса GET
        form = Goodform(initial={  # создадим форму со стартоввыми данными полей, соответствующими данным полей статьи
            'name': good.name,
            'category': good.category,
            'description': good.description,
            'remainder': good.remainder,
            'price': good.price

        })
        return render(request, 'change_good.html', context={'form': form, 'good': good})  # и отобразим форму редактирования статьи
    elif request.method == 'POST':  # Если метод запроса POST
        form = Goodform(data=request.POST)  # Создадим объект формы, в него передадим данные из формы, которые пришли от клиента
        if form.is_valid():
            good.name = form.cleaned_data.get('name')
            good.category = form.cleaned_data.get('category')
            good.description = form.cleaned_data.get('description')
            good.remainder = form.cleaned_data.get('remainder')
            good.price = form.cleaned_data.get('price')
            good.save()
            return redirect('see_good', pk=good.id)  # после сохранения статьи перенаправим на страницу просмотра статьи

        return render(request, 'change_good.html', context={'form': form, 'good': good})  # если форма не валидна - отобразим форму с ошибками


def good_delete():
    pass
