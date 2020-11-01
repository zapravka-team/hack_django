from django.urls import path


from .views import PetsView, ImageApiView, TestAPIView


urlpatterns = [
    path('', PetsView.as_view()),
    path('images/', ImageApiView.as_view()),
    path('api/', TestAPIView.as_view())
]