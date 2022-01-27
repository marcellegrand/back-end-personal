from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='IndexView'),
    path('series',views.SeriesView.as_view(),name='SeriesView'),
    path('serie/<int:serie_id>',views.SerieDetailView.as_view(),name='SerieDetailView')
]