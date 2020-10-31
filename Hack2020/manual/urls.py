from django.urls import path
from .views import SheltersView
from .views import OpOrgsView
from .views import PetTypesView
from .views import BreedsView
from .views import ColorsView
from .views import FursTypesView
from .views import EarTypesView
from .views import TailTypesView
from .views import DeathCausesView
from .views import DisposalCauseView
from .views import EuthanasiaCauseBookView

urlpatterns = [
    path('shelters/', SheltersView.as_view()),
    path('organizations/', OpOrgsView.as_view()),
    path('pettypes/', PetTypesView.as_view()),
    path('genders/', PetTypesView.as_view()),
    path('breeds/', BreedsView.as_view()),
    path('petcolors/', ColorsView.as_view()),
    path('furs/', FursTypesView.as_view()),
    path('ears/', EarTypesView.as_view()),
    path('tails/', TailTypesView.as_view()),
    path('deathcause/', DeathCausesView.as_view()),
    path('disposalcause/', DisposalCauseView.as_view()),
    path('euthanasiacause/', EuthanasiaCauseBookView.as_view())
]
