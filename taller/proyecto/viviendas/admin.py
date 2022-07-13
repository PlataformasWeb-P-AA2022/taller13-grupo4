from django.contrib import admin


# Importar las clases del modelo
from viviendas.models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad','tipo')
    search_fields = ('nombre', 'direccion')


admin.site.register(Edificio, EdificioAdmin)

class DepartametoAdmin(admin.ModelAdmin):

    list_display = ('nombre_propietario', 'costo_departamento', 'num_cuartos', 'edificio')

    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartametoAdmin)
