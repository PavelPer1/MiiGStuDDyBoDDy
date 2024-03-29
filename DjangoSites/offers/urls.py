from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:offer>/', views.page_offer, name='offer'),
    path('my_offers/', views.get_my_offers, name='my_offers'),
    path('my_offers/<str:room_name>/', views.room_view, name='room')
]