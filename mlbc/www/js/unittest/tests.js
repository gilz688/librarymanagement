'use strict';
var mod, injector, scope, bookController, http, q, service;

module("Book Controller Test", {
  setup: function() {
    mod = angular.module('mlbcApp', ['onsen']);
    injector = angular.injector(['ng', 'mlbcApp']);
	http = injector.get('$httpBackend');
	q = injector.get('$q');
	scope = injector.get('$rootScope').$new();
	service = injector.get('booksService');
	//bookController = injector.get('$controller')(booksController, { $scope: scope, $q: q, booksService: service }); 
  },
  teardown: function() {
    //todo
  }
});

test("Dummy Test", function() {
	//var $bookController = injector.get('$controller');
	//$bookController('booksController', {
	//	$scope: scope
	//});
	//equal(5, result, "okay");
	equal(1, 1, 'Passed');
});