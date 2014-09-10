var results;

function searchBook(){
	var keyword = $("#search_book").val();
	keyword = keyword.trim();
	results = 0;
	if(keyword==""){
		displayErrorMessage("Please don't leave blank.");
	}
	else{
		searchBookByTitle(keyword);
		searchBookByISBN(keyword);
		//searchBookByAuthor(keyword);
		$("#header").html("<h1>Search results for '" + keyword + "'</h1>");
		$("table#data-container").html("<tbody><tr><th style=\"text-align:center\">Book Title</th><th style=\"text-align:center\">ISBN</th></tr></tbody>");
	}
	$("#search_book").val("");
	return false;
}

function displayErrorMessage(text){
	toastr.options = {
  		"closeButton": true,
  		"debug": false,
  		"positionClass": "toast-bottom-right",
  		"onclick": null,
  		"showDuration": "300",
  		"hideDuration": "1000",
  		"timeOut": "5000",
  		"extendedTimeOut": "1000",
  		"showEasing": "swing",
  		"hideEasing": "linear",
  		"showMethod": "fadeIn",
  		"hideMethod": "fadeOut"
	};

	toastr.error(text, "Error!");
}