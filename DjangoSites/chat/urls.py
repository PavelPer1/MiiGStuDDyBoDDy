from django.contrib.auth.decorators import login_required
from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path('dialogs/', views.get_dialogs, name='dialogs'),
    path('dialogs/<num>', views.dialogs_views, name='dialogs_id')
]
