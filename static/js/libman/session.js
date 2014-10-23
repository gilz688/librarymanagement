function logInUser(event){
	event.preventDefault();
	var username = $("#username").val(),
		password = $("#password").val();
	validate(username, password);
}

function logOutUser(){
	$.ajax({
			type: "post",
			url: local_site+ "auth/logout",
			success: function(result){
				$("#panel_heading").html("");
				$("#panel_body").html("");
				viewUserHome();
			},
		});
}

function validate(username,password){
	if(checkIfNotBlank(username,password)){
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
				viewLibrarianHome(result.lib_name);
			},
			error: function(jqXHR, textStatus, errorThrown){
				if(jqXHR.status == 500){
					$("#sign-in-error").html("Invalid username and/or password");
					$("#password").val("");
				}
			}
		});
	}
	else{
		$("#sign-in-error").html("Username and Password field is required");
	}
}

function checkIfNotBlank(username,password){
	var username = username.trim();
	var	password = password.trim();

	if((username != "")&&(password != ""))
		return true;
	else
		return false;
}