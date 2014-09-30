function logInUser(){
	var username = $("#username").val(),
		password = $("#password").val();
	validate(username, password);
}

function logOutUser(){
	$.ajax({
			type: "post",
			url: local_site+ "auth/logout",
			success: function(result){
				$("#session a").html("Log In");
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
				$("#logInModal").modal('hide');
				$("#session a").html("Log Out");
			},
			error: function(jqXHR, textStatus, errorThrown){
				if(jqXHR.status == 500){
					$("#sign-in-error").html("Invalid Username or Password.");
					$("#password").val("");
				}
			}
		});
	}
	else{
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