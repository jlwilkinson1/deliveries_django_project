from django.contrib import admin
from .models import Offer, Restarantinfo

class FoodsAdmin(admin.ModelAdmin):
    list_display = ["__str__"]
    class Meta:
        model = Offer


admin.site.register(Offer, FoodsAdmin)
admin.site.register(Restarantinfo)
# Register your models here.
