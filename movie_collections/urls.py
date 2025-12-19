from django.urls import path
from .views import CollectionListCreateView, CollectionDetailView

urlpatterns = [
    path("collections/", CollectionListCreateView.as_view()),
    path("collections/<uuid:uuid>/", CollectionDetailView.as_view()),
]
