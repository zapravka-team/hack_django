from django.urls import path

from .views import AnimalCard
from .views import Summary
from .views import Monitoring

urlpatterns = [
    path('card/', AnimalCard.as_view()),
    path('summary/', Summary.as_view()),
    path('monitoring/', Monitoring.as_view())
]