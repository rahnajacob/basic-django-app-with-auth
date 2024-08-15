from django.urls import path
from .views import GameListCreateView

urlpatterns = [
    path('', GameListCreateView.as_view())
]