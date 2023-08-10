from rest_framework import serializers

from SandwichMenu.models import Sandwich


class SandwichSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sandwich
        fields = ('name', 'description', 'ingredients')
