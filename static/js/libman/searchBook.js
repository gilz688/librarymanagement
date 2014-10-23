var results;

function searchBook(){
	var keyword = $("#search-input").val();
	keyword = keyword.trim();
	results = 0;
	if(keyword==""){
		displayErrorMessage("Please don't leave blank.");
	}
	else{
		var mode = $("#mode-selected").val();
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
		$("#panel_heading").html("<b>Search results for '" + keyword + "'</b>");
	}
	$("#search-input").val("");
	return false;
}