from django.contrib.auth.views import LoginView
from django.urls import path
from accounts.views import logout_view, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('accounts/login', LoginView.as_view(), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/registration/', RegisterView.as_view(), name='registration'),

]

