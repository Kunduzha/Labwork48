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




def good_change():
    pass

def good_delete():
    pass
