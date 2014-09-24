var results;

function searchBook(){
	var keyword = $("#search_book").val();
	keyword = keyword.trim();
	results = 0;
	if(keyword==""){
		displayErrorMessage("Please don't leave blank.");
	}
	else{
		var mode=$("#selected").val();
		switch(mode){
			case "Title":
				searchBookByTitle(keyword);
				break;
			case "ISBN":
				searchBookByISBN(keyword);
				break;
			case "Author":
				searchBookByAuthor(keyword);
				break;
			default:
				searchBookByTitle(keyword);
		}
		$("#header").html("<h1>Search results for '" + keyword + "'</h1>");
		$("table#data-container").html("<tbody><tr><th style=\"text-align:center\">Book Title</th><th style=\"text-align:center\">ISBN</th></tr></tbody>");
	}
	$("#search_book").val("");
	return false;
}