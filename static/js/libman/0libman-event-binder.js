$(document).ready(function(){
	viewHome();
	$("#session").click(signInOrSignOut);
	$("#submitLogIn").click(logInUser);
	
	$("#borrow-button").click(borrowBookJS);
	$("#return-button").click(returnBookJS);
	$("#search_book").keypress(checkKey);
	$("#search").click(searchBook);
	$("#home").click(function(){
		viewHome();
	});
	$(".mode-menu").click(function(){
		var mode = $(this).children().first().html();
		$("#selected").val(mode);
		$("#searchMode").html(mode);
	});

	$("#logInModal").on('hidden.bs.modal', clearLoginModal);
	$("#bookInfo").on('hidden.bs.modal', clearBookModal);
});


function signInOrSignOut(){
	var session = $( "#session a" ).html();

	//if value == Log In then show Log In modal, else Log Out
	if(session == "Log In"){
		$("#logInModal").modal('show');
	}else{
		logOutUser();
	}
}


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

function borrowBookJS() {
    showConfirm("Borrow Book", "Are you sure you want to borrow a copy of this book?", function(){
    	borrowBook($("span#isbn").html());
    });
}

function returnBookJS() {
	showConfirm("Return Book", "Are you sure you want to return a copy of this book?", function(){
		returnBook($("span#isbn").html());
	});
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
	$("button#return-button").prop("disabled", true);
	$("button#borrow-button").prop("disabled", true);
}