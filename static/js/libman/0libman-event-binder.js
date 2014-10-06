$(document).ready(function(){
	viewHome();

	$("#home").click(viewHome);

	$("#session").click(signInOrSignOut);
	$("#submitLogIn").click(logInUser);
	
	$("#search-input").keypress(checkKey);
	$("#search-button").click(searchBook);

	$(".mode-menu").click(setSearchMode);

	$("#logInModal").on('hidden.bs.modal', clearLoginModal);
	$("#bookInfo").on('hidden.bs.modal', clearBookModal);
});



function viewHome(){
	$.ajax({
		type: "post",
		url: local_site+ "auth/getSession",
		dataType: "json",
		success: function(result){
			if(result != null){
				viewLibrarianHome(result.lib_name);
			}
			else{
				viewUserHome();
			}
		}
	});
}

function viewLibrarianHome(libraryName){
	getBooks(libraryName);
	$("#session a").html("Log Out");
}

function viewUserHome(){
	$("#session a").html("Log In");
	$("#header").html("<h1>Welcome to LIBMAN</h1><h2>This is a temporary Home Page for not Logged in users.</h2>");
	$("#data-container").html("");
}


function signInOrSignOut(){
	var session = $( "#session a" ).html();

	if(session == "Log In"){
		$("#logInModal").modal('show');
	}
	else{
		logOutUser();
	}
}


function checkKey(e){
	e.which
	var key = e.which;
 	if(key == 13)  // the enter key code
  	{
    	searchBook();
    	return false;
  	}
}

function setSearchMode(){
	var mode = $(this).children().first().html();
	$("#mode-selected").val(mode);
	$("#mode-selected b").html(mode);
}


function clearLoginModal(){
	$("#username").val("");
	$("#password").val("");
	$("#sign-in-error").html("");
}

function clearBookModal() {
	$("#isbn").html("");
	$("#myModalLabel").html("");
	$("#publisher").html("");
	$("#author").html("");
	$("#library").html("");
	$("#numcopies").html("");
	$("#status").html("");
	$("#availcopies").html("");
	$("#description").html("");
	$("#book_pic").attr("src", "#");
	$("#borrow-return-button").html("");
}