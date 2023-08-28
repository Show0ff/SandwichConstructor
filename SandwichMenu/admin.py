from django.contrib import admin

from .models import Sandwich
from .models import Ingredient

# Register your models here.

admin.site.register(Sandwich)
admin.site.register(Ingredient)
