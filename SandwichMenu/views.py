from django.shortcuts import render
from rest_framework import generics

from SandwichMenu.models import Sandwich
from SandwichMenu.serializer import SandwichSerializer


#

class SandwichAPIView(generics.ListAPIView):
    queryset = Sandwich.objects.all()
    serializer_class = SandwichSerializer
