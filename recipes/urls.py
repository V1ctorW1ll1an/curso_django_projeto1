from django.urls import path

from recipes.views import home_recipes

urlpatterns = [
    path('', home_recipes)
]
