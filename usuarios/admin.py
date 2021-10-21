from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "first_name", "last_name", "typo", "email")

admin.site.register(Account, AccountAdmin)