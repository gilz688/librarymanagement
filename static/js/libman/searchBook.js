function searchBook(e){
	e.which
	var key = e.which;
 	if(key == 13)  // the enter key code
  	{
    	var keyword = $("#search_book").val();
		searchBookByTitle(keyword);
		searchBookByISBN(keyword);
		$("#header").html("<h1>Search results for '" + keyword + "'</h1>");
		$("table#data-container").html("<tbody><tr><th style=\"text-align:center\">Book Title</th></tr></tbody>");
		$("#search_book").val("");
		return false;
  	}
}