'use strict';
var mod, injector, scope, bookController, http, q, service;

module("Book Controller Test", {
  setup: function() {
    mod = angular.module('mlbcApp', ['onsen']);
	mod.config(function ($provide) {
        $provide.decorator('$httpBackend', angular.mock.e2e.$httpBackendDecorator);
    });
	
    injector = angular.injector(['ng', 'mlbcApp']);
	//mock angular js services
	http = injector.get('$httpBackend');
	q = injector.get('$q');
	scope = injector.get('$rootScope').$new();
	
	//mock book service from app.js to books_service.js
	service = injector.get('booksService');
	
	//mock book controller from app.js to books_controller.js
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