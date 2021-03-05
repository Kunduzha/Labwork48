from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
def main_page(request):
    good=get_object_or_404()
    return render(request, "base.html", {'good':good})

def good_more(request, pk):
    good = get_object_or_404(Good, id=pk)
    return render(request, "good_more.html", {'good':good})


def good_add():
    good

def good_change():
    pass

def good_delete():
    pass
