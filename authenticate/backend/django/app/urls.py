from django.urls import path

from . import views

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

app_name = 'app'

urlpatterns = [
    path('',views.indexView.as_view()),
    path('usuario',views.UsuarioView.as_view()),
    path('registro',views.ClienteRegistroView.as_view()),
    path('acceder',views.UsuarioLoginView.as_view()),
    
    path('login',TokenObtainPairView.as_view()),
    path('refresh',TokenRefreshView.as_view()),
    path('verify',TokenVerifyView.as_view()),
]