function searchBook(){
	var keyword = $("#search_book").val();
	searchBookByTitle(keyword);
	searchBookByISBN(keyword);
	//searchBookByAuthor(keyword);
	$("#header").html("<h1>Search results for '" + keyword + "'</h1>");
	$("table#data-container").html("<tbody><tr><th style=\"text-align:center\">Book Title</th><th style=\"text-align:center\">ISBN</th></tr></tbody>");
	$("#search_book").val("");
	return false;
}