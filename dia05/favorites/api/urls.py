from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='IndexView'),
    path('favorite',views.FavoriteAllView.as_view(),name='FavoriteAllView'),
    path('public/favorite',views.PublicFavoriteAllView.as_view(),name='PublicFavoriteAllView'),
    path('favorite/<int:favorite_id>',views.FavoriteOneView.as_view(),name='FavoriteOneView'),
]