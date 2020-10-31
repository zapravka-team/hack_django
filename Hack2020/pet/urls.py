from django.urls import path

from .views import PetsView

urlpatterns = [
    path('', PetsView.as_view()),
]