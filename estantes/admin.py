from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Estante)
class EstanteAdmin(admin.ModelAdmin):
	list_display = ['id' ,'codigo', 'referencias', 'cantidad']
	search_fields = ['codigo', 'referencias']