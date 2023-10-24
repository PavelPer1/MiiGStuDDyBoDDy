from . import views
from django.urls import path, include

urlpatterns = [
    path('registration/', views.RegistrationUser.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login')
]