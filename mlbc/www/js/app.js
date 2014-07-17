(function(){
	'use strict';
	var app = angular.module('myApp', ['onsen.directives', 'ngTouch']);
 
	document.addEventListener('deviceready', function() {
		angular.bootstrap(document, ['myApp']);
	}, false);
})();
