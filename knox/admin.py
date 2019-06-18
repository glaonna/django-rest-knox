from django.contrib import admin


class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('digest', 'user', 'created',)
    fields = ()
    raw_id_fields = ('user',)
