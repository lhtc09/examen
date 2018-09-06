angular.module('salucita',['ui.router'])
.config(function($stateProvider,$urlRouterProvider){
	$stateProvider
	.state('home',{
		url: '/home',
		templateUrl: 'index.html'
	})
	.state('catalogo',{
		url: '/catalogo',
		templateUrl: '/views/catalogo.ejs'
	});
	$urlRouterProvider.otherwise('home');
})

.factory('comun', function($http){
	var comun = {};
	comun.usuarios = [];
	comun.usuario = {};

	/* Métodos para consumo de requerimientos */
	comun.eliminarusuario = function(usuario){
		return $http.delete('/usuarios/' + usuario._id)
		.then(function(){
			var indice = comun.usuarios.indexOf(usuario);
			comun.usuarios.splice(indice,1);
		})
	}
	comun.actualizausuario = function(usuario){
		return $http.put('/usuarios/' + usuario._id, usuario)
		.then(comun.usuarios.update(usuario))
	}
	comun.obtenerusuarios = function(){
		return $http.get('/usuarios')
		.then(function(res){
			var data = res.data;
			angular.copy(data, comun.usuarios)
			return comun.usuarios
		})
	}
	comun.agregarusuario = function(nuevousuario){
		return $http.post('/usuarios', nuevousuario)
		.then(comun.usuarios.push(nuevousuario))
	}
	comun.agregarproducto = function(nuevoproducto){
		return $http.post('/productos', nuevoproducto)
		.then(comun.usuarios.push(nuevoproducto))
	}
	comun.obtenerproductos = function(){
		return $http.get('/productos')
		.then(function(res){
			var data = res.data;
			angular.copy(data, comun.productos)
			return comun.productos
		})
	}
	return comun;
})

/* Controladores en página Registro */
.controller('ctrlregistro', function($scope,$state,comun){
	$scope.usuario = {};
	comun.obtenerusuarios();
	$scope.usuarios = comun.usuarios;


	$scope.agregarssuario = function(){
		comun.agregarusuario({
			cedula: $scope.usuario.cedula,
			nombres: $scope.usuario.nombres,
			email: $scope.usuario.email
		})
		$scope.usuario.cedula = '';
		$scope.usuario.nombres = '';
		$scope.usuario.email = '';
	}
	$scope.eliminarusuario = function(usuario){
		comun.eliminarusuario(usuario);
	}
	$scope.procesarusuario = function(usuario){
		comun.usuario = usuario;
		$state.go('editaru');
	}
})