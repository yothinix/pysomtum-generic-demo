from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'prefered_contact_method')
    list_filter = ('prefered_contact_method',)
    search_field = ('first_name', 'last_name', 'email', 'phone')
