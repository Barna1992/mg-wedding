from django.contrib import admin
from .models import Allergy

@admin.register(Allergy)
class AllergyAdmin(admin.ModelAdmin):
    list_display = ('nome', 'allergia')
    search_fields = ('nome', 'allergia')
