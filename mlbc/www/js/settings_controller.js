function settingsController($scope) {
    updateRemoteSite();
    $scope.remoteURL = remote_site;

    $scope.hideRemoteURLModal = function(choice){
    	if(choice == true)
    		setRemoteURL($scope.url);
    	remoteURLModal.hide();
    }

    $scope.showRemoteURLModal = function(){
    	$scope.url = getRemoteURL()
        remoteURLModal.show();
    };

    function setRemoteURL(url){
		window.localStorage.setItem("remote_url",url);
		remote_site = url;
		$scope.remoteURL = url;
	}
}