from behave import *
from src.cotizador import *

def before_scenario(context, scenario):
	context = {}

@given("que la ciudad del cliente es {ciudad}")
def step_impl(context,ciudad):
	context.ciudad = ciudad

@given("que la edad del cliente es {edad}")
def step_impl(context,edad):
	context.edad = int(edad)

@given("que el genero del cliente es {genero}")
def step_impl(context,genero):
	context.genero = genero

@given("que el estado civil del cliente es {estado}")
def step_impl(context,estado):
	context.estado = estado

@given("que el cliente tiene pre-existencias {preexistencias}")
def step_impl(context,preexistencias):
	context.preexistencias = preexistencias

@given("que el cliente tiene  {dependientes} dependientes")
def step_impl(context,dependientes):
	context.dependientes = int(dependientes)

@when("solicite la cotizacion")
def step_impl(context):
	resultado, mensaje = cotizar_seguro(context.ciudad,context.edad,context.genero,context.estado,context.preexistencias,context.dependientes)
	context.resultado = resultado
	context.mensaje = mensaje

@then("obtiene el mensaje '{mensaje}'")
def step_impl(context, mensaje):
	assert context.mensaje == mensaje