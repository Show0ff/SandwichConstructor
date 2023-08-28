from rest_framework import serializers

from SandwichMenu.models import Sandwich
from SandwichMenu.models import Ingredient


class SandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandwich
        fields = ('id','name', 'description', 'ingredients')


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'weight', 'kcal')


