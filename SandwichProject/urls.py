from django.contrib import admin
from django.urls import path

from SandwichMenu.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sandwich/all/', SandwichAPIList.as_view()),
    path('api/sandwich/delete/<int:pk>/', SandwichDeleteApiView.as_view()),
    path('api/ingredient/all', IngredientsApiList.as_view()),
    path('api/ingredient/delete/<int:pk>/', IngredientDeleteAPIView.as_view()),
]
