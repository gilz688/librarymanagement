function searchBookByISBN(isbn){
	$.ajax({
		url: local_site+ "searchBook/searchBookByISBN/" + isbn,
		dataType: "json",
		success: function(book_list_result){
			var book_list = "";
			for(var book in book_list_result){
				book_list += book_list_result[book].title;
			}
			alert(book_list);
		},
		error: function(e){
			alert(e);
		}
	});
}
