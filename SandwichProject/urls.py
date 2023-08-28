from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from SandwichMenu.views import *

router = routers.SimpleRouter()
router.register(r'sandwich', SandwichViewSet)
router.register(r'ingredient', IngredientViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
