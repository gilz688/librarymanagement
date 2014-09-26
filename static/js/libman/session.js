function logInUser(){
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
				
			},
		});
	$( "#session a" ).html("Log In"); // after mka log out i.change ang UI to Log In
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
	var username = username.trim(),
		password = password.trim();

	if((username != "")&&(password != ""))
		return true;
	else
		return false;
}