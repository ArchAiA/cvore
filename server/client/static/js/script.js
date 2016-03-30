// Angular module
var contractvore = angular.module('contractvore', ['ngRoute']);

// Clientside Routing
contractvore.config(function ($routeProvider, $locationProvider) {
	$routeProvider
		.when('/', {
			templateUrl: 'partials/contracts.html'
		})
		// .when('/contracts', {
		// 	templateUrl: 'partials/contracts2.html'
		// })
		.otherwise( {
			redirectTo: '/'
		});

	$locationProvider.html5Mode(true);
});

// Factories
contractvore.factory('ContractsFactory', function($http){
	var factory = {};

	factory.create_contract = function(info, callback){
		$http.post('/add_contract', info).success(function(output) {
			callback(output);
		})
	};

	factory.get_all = function(callback){
		$http.get('/get_contracts').success(function(output){
			callback(output);
		})
	};

	factory.delete_contract = function(info, callback){
		$http.post('/delete_contract', info).success(function(output) {
			callback(output);
		})
	};

	return factory;
})

// Client Controllers
contractvore.controller('ContractsController', function($scope, ContractsFactory) {
	$scope.addContract = function() {
		var contract_repack = { 
				state: $scope.new_contract.state, 
				contract_id: $scope.new_contract.contractid, 
				alternate_id: $scope.new_contract.alternateid, 
				contact_name: $scope.new_contract.contact_name, 
				description: $scope.new_contract.description, 
				purchase_method: $scope.new_contract.purchasemethod, 
				hidden: false, 
				created_at: new Date(),
				expires_at: $scope.new_contract.expiration
			};
		// We are passing a callback function which returns with data from the factory. This function will only execute if success from server
		ContractsFactory.create_contract(contract_repack, function(data){
			$scope.contracts = data;
		})
	}

	$scope.deleteContract = function(contract) {
		ContractsFactory.delete_contract(contract, function(data) {
			$scope.contracts = data;
		})
	}

	// Get all contracts through get_all factory function and pass to scope
	ContractsFactory.get_all(function(data){
		$scope.contracts = data;
	})
});