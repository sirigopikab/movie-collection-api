from django.urls import path
from .views import MoviesListView

urlpatterns = [
    path('movies/', MoviesListView.as_view(), name='movies'),
]
