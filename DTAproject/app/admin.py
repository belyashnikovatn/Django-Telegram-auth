from django.contrib import admin

from app.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'tlg_id',
        'tlg_name',
        'created_at'
    )
