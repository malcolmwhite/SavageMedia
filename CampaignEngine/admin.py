from django.contrib import admin

from django.contrib import admin

from models import Campaign


@admin.register(Campaign)
class Campaign(admin.ModelAdmin):
    pass