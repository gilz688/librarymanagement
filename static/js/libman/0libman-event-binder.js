$(document).ready(function(){

	$("#session").click(signInOrSignOut);
	$("#submitLogIn").click(logInUser);
	
	getBooks("COE-Library");
	$("#borrow-button").click(borrowBookJS);
	$("#search_book").keypress(checkKey);
	$("#search").click(searchBook);
	$("#home").click(function(){
		viewHome("COE-Library");
	});
	$(".mode-menu").click(function(){
		var mode = $(this).children().first().html();
		$("#selected").val(mode);
		$("#searchMode").html(mode);
	});

	$("#logInModal").on('hidden.bs.modal', clearLoginModal);
	$("#bookInfo").on('hidden.bs.modal', clearBookModal);
});


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

function viewHome(libraryName){
	$("#header").html("<h1>Welcome to "+libraryName+"</h1>");
	$("table#data-container").html("<tbody><tr><th style=\"text-align:center\">Book Title</th><th style=\"text-align:center\">ISBN</th></tr></tbody>");
	getBooks(libraryName);
}

function signInOrSignOut(){
	var session = $( "#session a" ).html();

	//if value == Log In then show Log In modal, else Log Out
	if(session == "Log In"){
		$("#logInModal").modal('show');
	}else{
		logOutUser();
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