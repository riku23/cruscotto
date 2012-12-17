from django.contrib import admin
from models import Url, Test,Verifica

class TestAdmin(admin.ModelAdmin):
    pass


class UrlAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ['name']}

class VerificaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Test, TestAdmin)

admin.site.register(Url, UrlAdmin)
admin.site.register(Verifica, VerificaAdmin)