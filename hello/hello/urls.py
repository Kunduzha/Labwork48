"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webapp.views.goods import IndexView_good, Good_more, Good_add, Good_change, Good_delete, AddToCart, Cart, DeleteFromCart
from webapp.views.orders import Checkout, CheckList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView_good.as_view(), name='main_page'),
    path('more/<int:pk>/', Good_more.as_view(), name='see_good'),
    path('add/', Good_add.as_view(), name='add_good'),
    path('edit/<int:pk>/', Good_change.as_view(), name='change_good'),
    path('delete/<int:pk>/', Good_delete.as_view(), name='del_good'),
    path('add_to_cart/<int:pk>', AddToCart.as_view(), name='add_to_cart'),
    path('in_cart/', Cart.as_view(), name='good_in_cart'),
    path('delete_from_cart/<int:pk>/', DeleteFromCart.as_view(), name='del_from_cart'),
    path('order/', Checkout.as_view(), name='checkout'),
    path('checklist/', CheckList.as_view(), name='checklist'),
    path('accounts/', include('accounts.urls')),
    path('api/v2/', include('api_v2.urls')),
]
