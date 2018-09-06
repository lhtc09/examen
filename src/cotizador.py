# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def calcular_cuota_basica(dependientes):
	"""Calcula la cuota basica del asegurado, 
	dependiendo de su numero de dependientes. 
    """
	cuota_basica = 0
	if dependientes == 0:
		cuota_basica = 30
	elif dependientes == 1:
		cuota_basica = 60
	elif dependientes == 2:
		cuota_basica = 90
	elif dependientes == 3:
		cuota_basica = 100
	elif dependientes == 4:
		cuota_basica = 120
	return cuota_basica

def calcular_valores_adicionales(edad, sexo, estado_civil, especial):
	"""Calcula los valores adicionales del asegurado, 
	dependiendo de su edad, sexo, estado civil y si 
	posee una pre-condición especial. 
    """
	valor_adicional = 0
	if edad >= 18 and edad <= 40:
		if sexo == 'mujer':
			if estado_civil == 'casado':
				valor_adicional = 20
			else:
				valor_adicional = 10
		else:
			if estado_civil == 'soltero':
				valor_adicional = 40
	elif edad >40 and edad<=60:
		if sexo == 'mujer':
			if especial == 'osteoporosis':
				valor_adicional = 35
		else:
			if especial == 'infarto':
				valor_adicional = 50
	elif edad >60:
		if especial in ['cancer','diabetes']:
			if sexo == 'mujer':
				valor_adicional = 60
			else:
				valor_adicional = 50
	return valor_adicional

def cotizar_seguro(ciudad, edad, sexo, estado_civil, especial, dependientes):
	"""Calcula el valor total del sguro cotizado al asegurado, 
	dependiendo de su edad, sexo, estado civil, ciudad, numero de dependientes
	y si posee una pre-condición especial. 
    """
	valor_total = 0.0
	if ciudad in ['Guayaquil','Quito','Cuenca','Machala']:
		if dependientes <= 4:
			if edad>=18 and edad<=75:
				cuota_basica = calcular_cuota_basica(dependientes)
				valor_adicional = calcular_valores_adicionales(edad, sexo, estado_civil, especial)
				valor_total = cuota_basica + valor_adicional
				resultado = "El valor calculado de su cotización es de %.2f" % valor_total
			else:
				resultado = "La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años."
		elif dependientes <=9 and dependientes > 4:
			resultado = "Solo se puede realizar la cotización para hasta 4 dependientes en línea. \
			Por favor acérquese a la agencia y presente una solicitud."
		else:
			resultado = "No se puede realizar una cotización para el valor ingresado de dependientes."
	else:
		resultado = "Saludcita no opera en la ciudad ingresada."
	return resultado