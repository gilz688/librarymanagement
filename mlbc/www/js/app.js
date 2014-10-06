var remote_site = "http://192.168.1.36:8000/librarymanagement/";
var app = angular.module('mlbcApp', ['onsen']);

app.controller("booksController", booksController);
app.controller("settingsController", settingsController);
app.service("booksService", booksService);

document.addEventListener("deviceready", onDeviceReady, false);

// Cordova is ready
function onDeviceReady() {
	updateRemoteSite();
}

function getRemoteURL(){
	return window.localStorage.getItem("remote_url");
}

function updateRemoteSite(){
	var remote_url = getRemoteURL();
    if(remote_url == null)
    	 window.localStorage.setItem("remote_url", remote_site);
    else
    	remote_site = remote_url;
}