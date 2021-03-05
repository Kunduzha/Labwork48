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
from django.urls import path
from webapp.views import main_page, good_more, good_add, good_change, good_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='all_page'),
    path('more/<int:pk>/', good_more, name='see_good'),
    path('add/', good_add, name='add_good'),
    path('edit/<int:pk>/', good_change, name='change_good'),
    path('delete/<int:pk>/', good_more, name='del_good')
]
