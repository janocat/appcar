from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Auto(models.Model):
	id_car = models.IntegerField()
	marca = models.CharField(max_length=50)
	mmv = models.CharField(max_length=150)
	precio_lista = models.IntegerField(blank=True, null=True)
	bono_marca = models.IntegerField(blank=True, null=True)
	valor_final_c = models.IntegerField(blank=True, null=True)
	bono_financiacion = models.IntegerField(blank=True, null=True)
	precio_bd_bf = models.IntegerField(blank=True, null=True)
	fecha = models.DateField(blank=True, null=True)

	##class Meta:
	##	ordering = ('-marca',)
	def __str__(self):
		template = '{0.id_car} {0.marca} {0.mmv} {0.precio_lista} {0.bono_marca} {0.valor_final_c} {0.bono_financiacion} {0.precio_bd_bf} {0.fecha}' ##{0.concesionario} {0.vendedor} {0.telefono}'
		return template.format(self)
