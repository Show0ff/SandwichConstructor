from rest_framework import generics, status
from rest_framework.response import Response

from SandwichMenu.models import Sandwich
from SandwichMenu.serializer import SandwichSerializer
from SandwichMenu.models import Ingredient
from SandwichMenu.serializer import IngredientSerializer



class SandwichAPIList(generics.ListCreateAPIView):
    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer

class SandwichDeleteApiView(generics.DestroyAPIView):
    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientsApiList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class IngredientDeleteAPIView(generics.DestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)