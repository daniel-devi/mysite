from django.contrib import admin
from .models import Products,Brand,Address,Category,Feedback

# Register your models here.

class productAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title","price", "id")
    list_filter = ("is_best_seller",)
    search_fields = ("title","category","brand")

admin.site.register(Brand)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Feedback)
admin.site.register(Products,productAdmin)
