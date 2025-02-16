from django.urls import path
from .views import get_chain

urlpatterns = [
    path('chain/', get_chain),
]
