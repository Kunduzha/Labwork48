from django.shortcuts import render

# Create your views here.
def main_page(request):
    if request.method=="GET":
        return render(request, "base.html")

def good_more():
    pass

def good_add():
    pass

def good_change():
    pass

def good_delete():
    pass
