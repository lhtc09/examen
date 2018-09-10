# language: es

Característica: Cotizar hombres solteros.

  @hombres_solteros

   Escenario: Hombre soltero de la ciudad de Esmeraldas de 22 años con 4 dependientes y pre-existencias cancer
      Dado que la ciudad del cliente es Esmeraldas
      Dado que la edad del cliente es 22
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente tiene pre-existencia cancer
      Dado que el cliente tiene 4 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'Saludcita no opera en la ciudad ingresada'

   Escenario: Hombre soltero de la ciudad de Quito de 17 años con 0 dependientes y pre-existencias osteoporosis
      Dado que la ciudad del cliente es Quito
      Dado que la edad del cliente es 17
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente tiene pre-existencia osteoporosis
      Dado que el cliente tiene 0 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'La edad ingresada no es válida. La edad permitida es entre 18 y 75 años'

   Escenario: Hombre soltero de la ciudad de Cuenca de 90 años con 3 dependientes e infarto de pre-existencia 
      Dado que la ciudad del cliente es Cuenca
      Dado que la edad del cliente es 90
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente tiene pre-existencia infarto
      Dado que el cliente tiene 3 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'La edad ingresada no es válida. La edad permitida es entre 18 y 75 años'

   Escenario: Hombre soltero de la ciudad de Machala de 29 años con 5 dependientes sin pre-existencia 
      Dado que la ciudad del cliente es Machala
      Dado que la edad del cliente es 29
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente no tiene pre-existencia
      Dado que el cliente tiene 5 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'El número de dpendientes supera el permitido para su cotización en línea. Un ejecutivo se comunicará con usted.'

   Escenario: Hombre soltero de la ciudad de Cuenca de 33 años con 10 dependientes y pre-existencia cancer
      Dado que la ciudad del cliente es Cuenca
      Dado que la edad del cliente es 33
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente tiene pre-existencia cancer
      Dado que el cliente tiene 10 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'El número de dpendientes no está permitido. Debe ingresar un número entre 0 y 9.'

   Escenario: Hombre soltero de la ciudad de Guayaquil de 24 años con 2 dependientes sin pre-existencia.
      Dado que la ciudad del cliente es Guayaquil
      Dado que la edad del cliente es 24
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente no tiene pre-existencia
      Dado que el cliente tiene 2 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'El valor calculado de su cotización es de 130'

   Escenario: Hombre soltero de la ciudad de Machala de 50 años con 2 dependientes con infarto de pre-existencia 
      Dado que la ciudad del cliente es Machala
      Dado que la edad del cliente es 50
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente tiene pre-existencia infarto
      Dado que el cliente tiene 2 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'El valor calculado de su cotización es de 140'

   Escenario: Hombre soltero de la ciudad de Cuenca de 50 años con 2 dependientes con osteoporosis de pre-existencia 
      Dado que la ciudad del cliente es Cuenca
      Dado que la edad del cliente es 50
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente tiene pre-existencia osteoporosis
      Dado que el cliente tiene 2 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'El valor calculado de su cotización es de 90'

   Escenario: Hombre soltero de la ciudad de Guayaquil de 71 años con 2 dependientes con diabetes de pre-existencia 
      Dado que la ciudad del cliente es Guayaquil
      Dado que la edad del cliente es 71
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente tiene pre-existencia diabetes
      Dado que el cliente tiene 2 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'El valor calculado de su cotización es de 150'

   Escenario: Hombre soltero de la ciudad de Quito de 73 años con 2 dependientes con osteoporosis de pre-existencia 
      Dado que la ciudad del cliente es Quito
      Dado que la edad del cliente es 73
      Dado que el genero del cliente es hombre
      Dado que el estado civil del cliente es soltero
      Dado que el cliente tiene pre-existencia osteoporosis
      Dado que el cliente tiene 2 dependientes 
      Cuando solicite la cotizacion 
      Entonces obtiene el mensaje 'El valor calculado de su cotización es de 90'

   