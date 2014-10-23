function searchBookByAuthor(author){
	$.ajax({
		type: "post",
		url: local_site+ "searchBook/searchByAuthor/",
		data: {
			"author" : author,
		},
		dataType: "json",
		success: function(books){
			displaySearchedBooks(books,author);
		},
		error: function(e){
			$("#panel_body").html("<b>No book Found.</b>");
			if(results == 0){
				displayErrorMessage("Not found!");
			}
		}
	});
}