from django.urls import path
from . import views

urlpatterns = [
    path('<int:offer>/', views.page_offer, name='offer')
]