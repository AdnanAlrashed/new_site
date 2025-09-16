from django.contrib import admin
from . models import StolenCredential
# Register your models here.
@admin.register(StolenCredential)
class StolenCredentialAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'timestamp')
    search_fields = ('username',)
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
