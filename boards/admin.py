from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

from .models import Auto

class AutoResource(resources.ModelResource):
    id_car = fields.Field(attribute='id_car', column_name='Nº')
    marca = fields.Field(attribute='marca', column_name='Marca')
    mmv = fields.Field(attribute='mmv', column_name='MMV')
    precio_lista = fields.Field(attribute='precio_lista', column_name='Precio Lista')
    bono_marca = fields.Field(attribute='bono_marca', column_name='Bono Marca')
    valor_final_c = fields.Field(attribute='valor_final_c', column_name='Bono Financiamiento')
    precio_bd_bf = fields.Field(attribute='precio_bd_bf', column_name='Precio con Bono Directo + Bono Financiamiento')
    fecha = fields.Field(attribute='fecha', column_name='Fecha')

    class Meta:
        model = Auto
        fields = (
            'id_car', 
            'marca', 
            'mmv', 
            'precio_lista', 
            'bono_marca', 
            'valor_final_c', 
            'bono_financiacion', 
            'precio_bd_bf', 
            'fecha',) 

        export_order = fields
        import_id_fields = ('id_car',)

class AutoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Auto
    resource_class = AutoResource
    list_display = [
    'get_id_car', 
    'get_marca', 
    'get_mmv', 
    'get_precio_lista', 
    'get_bono_marca', 
    'get_valor_final_c', 
    'get_bono_financiacion', 
    'get_precio_bd_bf', 
    'get_fecha'] 

    list_filter = (
    	'id_car', 
        'marca', 
        'mmv', 
        'precio_lista', 
        'bono_marca', 
        'valor_final_c', 
        'bono_financiacion', 
        'precio_bd_bf', 
        'fecha') 
        ##'concesionario', 


    def get_id_car(self, obj):
        return obj.id_car
    def get_marca(self, obj):
        return obj.marca
    def get_mmv(self, obj):
        return obj.mmv
    def get_precio_lista(self, obj):
        return obj.precio_lista
    def get_bono_marca(self, obj):
        return obj.bono_marca
    def get_valor_final_c(self, obj):
        return obj.valor_final_c
    def get_bono_financiacion(self, obj):
        return obj.bono_financiacion
    def get_precio_bd_bf(self, obj):
        return obj.precio_bd_bf
    def get_fecha(self, obj):
        return obj.fecha

    get_id_car.admin_order_field  = 'id_car'
    get_id_car.short_description = 'Nº' 
    get_marca.short_description = 'Marca' 
    get_mmv.short_description = 'MMV' 
    get_precio_lista.short_description = 'Precio Lista' 
    get_bono_marca.short_description = 'Bono Marca' 
    get_valor_final_c.short_description = 'Valor Final Contado' 
    get_bono_financiacion.short_description = 'bono_financiacion' 
    get_precio_bd_bf.short_description = 'Precio con Bono Directo + Bono Financiamiento' 
    get_fecha.short_description = 'Fecha' 

admin.site.register(Auto, AutoAdmin)