$(document).ready(function(){
	viewHome();

	$("#borrowListData").hide();
	$("#historyListData").hide();

	$("#borrowList").click(viewBorrowOption);
	$("#historyList").click(viewHistoryOption);


	$("#home").click(viewHome);

	$("#session").click(signInOrSignOut);
	$("#submitLogIn").click(logInUser);
	
	$("#search-input").keypress(checkKey);
	$("#search-button").click(searchBook);

	$(".mode-menu").click(setSearchMode);

	$("#logInModal").on('hidden.bs.modal', clearLoginModal);
	$("#bookInfo").on('hidden.bs.modal', clearBookModal);
});

function viewBorrowOption(){
	if($("#borrowListData").is(':visible'))
		$("#borrowListData").hide('slow');
	else
		$("#borrowListData").show('slow');

	$("#historyListData").hide('slow');
}

function viewHistoryOption(){
	if($("#historyListData").is(':visible'))
		$("#historyListData").hide('slow');
	else
		$("#historyListData").show('slow');

	$("#borrowListData").hide('slow');
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
	viewGenerateReportOptionsLoggedIn();
	$("#session a").html("Log Out");
}

function viewUserHome(){
	$("#session a").html("Log In");
	$("#header").html("<h1>Welcome to LIBMAN</h1><h2>This is a temporary Home Page for not Logged in users.</h2>");
	$("#data-container").html("");
	viewGenerateReportOptionsNotLoggedIn();
}

/*
function viewGenerateReportOptionsNotLoggedIn() {
	var yearOption = "<li><a href=\"#\" onclick= 'testAlert(\"Year\");'> Year <a></li>";
	var monthOption = "<li><a href=\"#\" onclick= 'testAlert(\"Month\");'> Month </a></li>";
	var dayOption = "<li><a href=\"#\" onclick= 'testAlert(\"Day\");'> Day </a></li>";
	$("#report_options").html('Get most borrowed book by: <div class="most_borrowed_book_options">	<ul> '+ yearOption + monthOption + dayOption + '</ul></div>');
}

function viewGenerateReportOptionsLoggedIn() {
	var yearOption = "<li><a href=\"#\" onclick= 'testAlert(\"Year\");'> Year <a></li>";
	var monthOption = "<li><a href=\"#\" onclick= 'testAlert(\"Month\");'> Month </a></li>";
	var dayOption = "<li><a href=\"#\" onclick= 'testAlert(\"Day\");'> Day </a></li>";
	$("#report_options").html('Get most borrowed book by: <div class="most_borrowed_book_options">	<ul>' + yearOption + monthOption + dayOption + '</ul> </div>Get library report by: <div class="most_borrowed_book_options"> <ul>' + yearOption + monthOption + dayOption + '</ul> </div>');
}
*/
function testAlert(option) {
	alert(option);
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