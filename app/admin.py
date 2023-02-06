from django.contrib import admin
from .models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    search_fields = ['nome']
    list_per_page = 8



admin.site.register(Pessoa, PessoaAdmin)