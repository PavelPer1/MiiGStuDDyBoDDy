from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.urls import path, include

urlpatterns = [
    path('registration/', views.RegistrationUser.as_view(), name='registration'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('create_profile/', views.CreateProfile.as_view(), name='create_profile'),
    path('profile/', views.profile_view, name='profile')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
