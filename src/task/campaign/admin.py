from django.contrib import admin
from .models import Campaign
# Register your models here.

class CompaignAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_filter = ["name"]


admin.site.register(Campaign)