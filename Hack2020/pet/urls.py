from django.urls import path

from rest_framework.schemas.openapi import AutoSchema
from rest_framework_swagger.views import get_swagger_view
from .views import PetsView, ImageApiView, TestAPIView

auto_schema = get_swagger_view(title='lol')

urlpatterns = [
    path('', PetsView.as_view()),
    path('swagger/', auto_schema),
    path('images/', ImageApiView.as_view()),
    path('api/', TestAPIView.as_view())
]