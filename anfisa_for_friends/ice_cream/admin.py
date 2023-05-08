from django.contrib import admin

# Register your models here.
from .models import Category
from .models import IceCream
from .models import Topping
from .models import Wrapper

admin.site.register(Category)
admin.site.register(IceCream)
admin.site.register(Topping)
admin.site.register(Wrapper)
