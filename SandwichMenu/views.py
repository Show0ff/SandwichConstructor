from rest_framework import generics, status, viewsets

from SandwichMenu.models import Sandwich
from SandwichMenu.serializer import SandwichSerializer
from SandwichMenu.models import Ingredient
from SandwichMenu.serializer import IngredientSerializer


class SandwichViewSet(viewsets.ModelViewSet):
    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
