from django.urls import path
from .views import SheltersView
from .views import OpOrgView
from .views import AnimalTView
from .views import AnimalSexBookView
from .views import BreedsBookView
from .views import AnimalColorsBookView
from .views import FurTBookView
from .views import EarTBookView
from .views import TailTBookView
from .views import DeathCauseBookView
from .views import DisposalCauseBookView
from .views import EuthanasiaCauseBookView

urlpatterns = [
    path('shelters/', SheltersView.as_view()),
    path('organizations/', OpOrgView.as_view()),
    path('animaltypes/', AnimalTView.as_view()),
    path('genders/', AnimalSexBookView.as_view()),
    path('breeds/', BreedsBookView.as_view()),
    path('animalcolors/', AnimalColorsBookView.as_view()),
    path('furs/', FurTBookView.as_view()),
    path('ears/', EarTBookView.as_view()),
    path('tails/', TailTBookView.as_view()),
    path('deathcause/', DeathCauseBookView.as_view()),
    path('disposalcause/', DisposalCauseBookView.as_view()),
    path('euthanasiacause/', EuthanasiaCauseBookView.as_view())
]