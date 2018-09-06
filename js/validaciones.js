function numdependientes(){
		var dependientes = document.datosseguro.dependientes.value;
		var cuotaxdependientes = document.datosseguro.cuotaxdependientes.value;
		switch (dependientes) {
			case 0:
			cuotaxdependientes = 30;
			[break];
			case 1:
			cuotaxdependientes = 60;
			[break];
			case 2:
			cuotaxdependientes = 90;
			[break];
			case 3:
			cuotaxdependientes = 100;
			[break];
			case 4:
			cuotaxdependientes = 120;
			[break];
			default:
			cuotaxdependientes = 0;
			[break];
		}
		return cuotaxdependientes;
	}
function calcular(){
	var edad = document.datosseguro.edad.value;
	var sexo = document.datosseguro.sexo.value;
	var civil = document.datosseguro.civil.value;
	var preexistencias = document.datosseguro.preexistencias.value;
	var dependientes = document.datosseguro.dependientes.value;
	var couta=0;
	if(edad>=18 && edad<=40){
		if(sexo=="F"){
			if(civil=="Casado"){
				couta=20;
			}else{
				cuota=10
			}
		}else{
			if (civil=="Soltero") {}
		}
	}

}
function validaedad(){
   var edad = document.datosseguro.edad.value;
   if (edad < 18 || edad > 75){
      alert("No tiene edad requerida para contratar un seguro.");
      return false;
  }
  return true;
}
function validadependientes(){
	var dependientes = document.datosseguro.dependientes.value;
	if(dependientes<0 || dependientes>9){
		alert("Debe ingresar un número entero entre 0 y 9");
		return false;
	}
	return true;
}