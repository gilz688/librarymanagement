function searchBookByTitle(book_title){
	$.ajax({
		type: "post",
		url: local_site+ "searchBook/searchBookByTitle/",
		data: {
			"keyword" : book_title,
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
