function searchBookByAuthor(author){
	$.ajax({
		type: "post",
		url: local_site+ "searchBook/searchByAuthor/",
		data: {
			"author" : author,
		},
		dataType: "json",
		success: function(books){
			displayBooks(books);
		},
		error: function(e){
			if(results == 0){
				displayErrorMessage("Not found!");
			}
		}
	});
}