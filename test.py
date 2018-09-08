# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from src.cotizador import *

class Test(unittest.TestCase):
	#Incluya una pequeña descripción de lo que se prueba.
	def test_cotizador_ID(self):
		self.assertEqual('','')

	#Ciudad diferente a las del arreglo en que opera Saludcita
	def test_cotizador_ciudad_no_servicio(self):
		self.assertEqual(cotizar_seguro('Esmeraldas', 30, 'mujer', 'soltero', 'infarto', 2),"Saludcita no opera en la ciudad ingresada.")

	#Edad no admitida para cotizar seguro
	def test_cotizador_edad_inadmisible(self):
		self.assertEqual(cotizar_seguro('Quito', 80, 'mujer', 'soltero', 'infarto', 2),"La edad ingresada no es válida. Debe de encontrarse entre 18 y 75 años.")

	#Dependientes no admitidos para cotizar seguro
	def test_cotizador_dependientes_inadmisibles(self):
		self.assertEqual(cotizar_seguro('Cuenca', 20, 'hombre', 'casado', 'infarto', 11),"No se puede realizar una cotización para el valor ingresado de dependientes.")

	#Dependientes no admitidos para cotizar directaente el seguro
	def test_cotizador_dependientes_por_revisiom(self):
		self.assertEqual(cotizar_seguro('Quito', 25, 'mujer', 'soltero', 'infarto', 6),"Solo se puede realizar la cotización para hasta 4 dependientes en línea. Por favor acérquese a la agencia y presente una solicitud.")

	#Seguro para caso A10: mujer casada de entre 18 y 40 y sin dependientes
	def test_cotizador_caso_a10(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'casado', 'infarto', 0),50)

	#Seguro para caso A11: mujer casada de entre 18 y 40 y con 1 dependiente
	def test_cotizador_caso_a11(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'casado', 'infarto', 1),80)

	#Seguro para caso A12: mujer casada de entre 18 y 40 y con 2 dependientes
	def test_cotizador_caso_a12(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'casado', 'infarto', 2),110)

	#Seguro para caso A13: mujer casada de entre 18 y 40 y con 3 dependientes
	def test_cotizador_caso_a13(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'casado', 'infarto', 3),120)

	#Seguro para caso A14: mujer casada de entre 18 y 40 y con 4 dependientes
	def test_cotizador_caso_a14(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'casado', 'infarto', 4),140)

	#Seguro para caso A20: mujer soltera, viuda o divorciada de entre 18 y 40 y sin dependientes
	def test_cotizador_caso_a20(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'soltero', 'infarto', 0),40)

	#Seguro para caso A21: mujer soltera, viuda o divorciada de entre 18 y 40 y con 1 dependiente
	def test_cotizador_caso_a21(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'soltero', 'infarto', 1),70)

	#Seguro para caso A22: mujer soltera, viuda o divorciada de entre 18 y 40 y con 2 dependientes
	def test_cotizador_caso_a22(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'soltero', 'infarto', 2),100)

	#Seguro para caso A23: mujer soltera, viuda o divorciada de entre 18 y 40 y con 3 dependientes
	def test_cotizador_caso_a23(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'soltero', 'infarto', 3),110)

	#Seguro para caso A24: mujer soltera, viuda o divorciada de entre 18 y 40 y con 4 dependientes
	def test_cotizador_caso_a24(self):
		self.assertEqual(cotizar_seguro('Cuenca', 30, 'mujer', 'soltero', 'infarto', 4),130)

	#Seguro para caso B0: hombre solter de entre 18 y 40 y sin dependientes
	def test_cotizador_caso_b0(self):
		self.assertEqual(cotizar_seguro('Quito', 35, 'hombre', 'soltero', 'infarto', 0),70)

	#Seguro para caso B1: hombre soltero de entre 18 y 40 y con 1 dependiente
	def test_cotizador_caso_b1(self):
		self.assertEqual(cotizar_seguro('Quito', 35, 'hombre', 'soltero', 'infarto', 1),100)

	#Seguro para caso B2: hombre soltero de entre 18 y 40 y con 2 dependientes
	def test_cotizado_caso_b2r(self):
		self.assertEqual(cotizar_seguro('Quito', 35, 'hombre', 'soltero', 'infarto', 2),130)

	#Seguro para caso B3: hombre soltero de entre 18 y 40 y con 3 dependientes
	def test_cotizador_caso_b3(self):
		self.assertEqual(cotizar_seguro('Quito', 35, 'hombre', 'soltero', 'infarto', 3),140)

	#Seguro para caso B4: hombre soltero de entre 18 y 40 y con 4 dependientes
	def test_cotizado_caso_b4(self):
		self.assertEqual(cotizar_seguro('Quito', 35, 'hombre', 'soltero', 'infarto', 4),160)

	#Seguro para caso C0: mujer de cualquier estado civil de entre 41 y 60, con osteoporosis y sin dependientes
	def test_cotizador_caso_c0(self):
		self.assertEqual(cotizar_seguro('Machala', 45, 'mujer', 'soltero', 'osteoporosis', 0),65)

	#Seguro para caso C1: mujer de cualquier estado civil de entre 41 y 60, con osteoporosis y con 1 dependiente
	def test_cotizador_caso_c1(self):
		self.assertEqual(cotizar_seguro('Machala', 45, 'mujer', 'casado', 'osteoporosis', 1),95)

	#Seguro para caso C2: mujer de cualquier estado civil de entre 41 y 60, con osteoporosis y con 2 dependientes
	def test_cotizador_caso_c2(self):
		self.assertEqual(cotizar_seguro('Machala', 45, 'mujer', 'viudo', 'osteoporosis', 2),125)

	#Seguro para caso C3: mujer de cualquier estado civil de entre 41 y 60, con osteoporosis y con 3 dependientes
	def test_cotizador_cas0_c3(self):
		self.assertEqual(cotizar_seguro('Machala', 45, 'mujer', 'soltero', 'osteoporosis', 3),135)

	#Seguro para caso C4: mujer de cualquier estado civil de entre 41 y 60, con osteoporosis y con 4 dependientes
	def test_cotizador_cas0_c4(self):
		self.assertEqual(cotizar_seguro('Machala', 45, 'mujer', 'soltero', 'osteoporosis', 4),155)

	#Seguro para caso D0: mujer de cualquier estado civil de entre 41 y 60, con infarto y sin dependientes
	def test_cotizador_cas0_d0(self):
		self.assertEqual(cotizar_seguro('Guayaquil', 50, 'mujer', 'soltero', 'infarto', 0),80)

	#Seguro para caso D1: mujer de cualquier estado civil de entre 41 y 60, con infarto y con 1 dependiente
	def test_cotizador_caso_d1(self):
		self.assertEqual(cotizar_seguro('Guayaquil', 50, 'mujer', 'soltero', 'infarto', 1),110)

	#Seguro para caso D2: mujer de cualquier estado civil de entre 41 y 60, con infarto y con 2 dependientes
	def test_cotizador_caso_d2(self):
		self.assertEqual(cotizar_seguro('Guayaquil', 50, 'mujer', 'soltero', 'infarto', 2),140)

	#Seguro para caso D3: mujer de cualquier estado civil de entre 41 y 60, con infarto y con 3 dependientes
	def test_cotizador_caso_d3(self):
		self.assertEqual(cotizar_seguro('Guayaquil', 50, 'mujer', 'soltero', 'infarto', 3),150)

	#Seguro para caso D4: mujer de cualquier estado civil de entre 41 y 60, con infarto y con 4 dependientes
	def test_cotizador_caso_d4(self):
		self.assertEqual(cotizar_seguro('Guayaquil', 50, 'mujer', 'soltero', 'infarto', 4),170)

	#Seguro para caso E0: mujer de cualquier estado civil de entre 61 y 75, con cancer o diabetes y sin dependientes
	def test_cotizador_cas0_e0(self):
		self.assertEqual(cotizar_seguro('Cuenca', 70, 'mujer', 'casado', 'diabetes', 0),80)

	#Seguro para caso E1: mujer de cualquier estado civil de entre 61 y 75, con cancer o diabetes y con 1 dependiente
	def test_cotizador_cas0_e1(self):
		self.assertEqual(cotizar_seguro('Cuenca', 70, 'mujer', 'casado', 'diabetes', 1),110)

	#Seguro para caso E2: mujer de cualquier estado civil de entre 61 y 75, con cancer o diabetes y con 2 dependientes
	def test_cotizador_cas0_e2(self):
		self.assertEqual(cotizar_seguro('Cuenca', 70, 'mujer', 'casado', 'cancer', 2),140)

	#Seguro para caso E3: mujer de cualquier estado civil de entre 61 y 75, con cancer o diabetes y con 3 dependientes
	def test_cotizador_cas0_e3(self):
		self.assertEqual(cotizar_seguro('Cuenca', 70, 'mujer', 'casado', 'diabetes', 3),150)

	#Seguro para caso E4: mujer de cualquier estado civil de entre 61 y 75, con cancer o diabetes y con 4 dependientes
	def test_cotizador_cas0_e4(self):
		self.assertEqual(cotizar_seguro('Cuenca', 70, 'mujer', 'casado', 'diabetes', 4),170)

	#Seguro para caso F0: hombre de cualquier estado civil de entre 61 y 75, con cancer o diabetes y sin dependientes
	def test_cotizador_cas0_f0(self):
		self.assertEqual(cotizar_seguro('Quito', 64, 'hombre', 'soltero', 'cancer', 0),90)

	#Seguro para caso F1: hombre de cualquier estado civil de entre 61 y 75, con cancer o diabetes y con 1 dependiente
	def test_cotizador_cas0_f1(self):
		self.assertEqual(cotizar_seguro('Quito', 64, 'hombre', 'soltero', 'cancer', 1),120)

	#Seguro para caso F2: hombre de cualquier estado civil de entre 61 y 75, con cancer o diabetes y con 2 dependientes
	def test_cotizador_cas0_f2(self):
		self.assertEqual(cotizar_seguro('Quito', 64, 'hombre', 'soltero', 'cancer', 2),150)

	#Seguro para caso F3: hombre de cualquier estado civil de entre 61 y 75, con cancer o diabetes y con 3 dependientes
	def test_cotizador_cas0_f3(self):
		self.assertEqual(cotizar_seguro('Quito', 64, 'hombre', 'soltero', 'cancer', 3),160)

	#Seguro para caso F4: hombre de cualquier estado civil de entre 61 y 75, con cancer o diabetes y con 4 dependientes
	def test_cotizador_cas0_f4(self):
		self.assertEqual(cotizar_seguro('Quito', 64, 'hombre', 'soltero', 'cancer', 4),180)


if __name__ == '__main__':
	unittest.main()
