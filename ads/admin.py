from django.contrib import admin

# Register your models here.
from ads.models import User
from ads.models.ad import Ad

class AdAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'description',
        'price',
    ]


admin.site.register(Ad)
admin.site.register(User)
