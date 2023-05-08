from django.contrib import admin

from .models import Category
from .models import IceCream
from .models import Topping
from .models import Wrapper


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'
    filter_horizontal = ('toppings',)


admin.site.register(Category)
admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Topping)
admin.site.register(Wrapper)
