function logInUser(){
	//for testing purposes only
	$("#logInModal").modal('hide');
	$( "#session a" ).html("Log Out");
}

function logOutUser(){
	$.ajax({
			type: "post",
			url: local_site+ "auth/logout",
			data: {
				
			},
			dataType: "json",
			success: function(result){
				$( "#session a" ).html("Log In");
			},
		});
}


function validate(username,password){
	if(checIfnotBlank(username,password)){
		$.ajax({
			type: "post",
			url: local_site+ "auth/login",
			data: {
				username: username,
				password: password
			},
			dataType: "json",
			success: function(result){
				//some codes here..
			},
		});
	}
	else{
		//displays error in modal
		$("#sign-in-error").html("Username and Password field is required.");
	}
	
}

function checIfnotBlank(username,password){
	var username = username.trim();
	var	password = password.trim();

	if((username != "")&&(password != ""))
		return true;
	else
		return false;
}