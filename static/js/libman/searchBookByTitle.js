function searchBookByTitle(book_title){
	$.ajax({
		type: "post",
		url: local_site+ "searchBook/searchBookByTitle/" + book_title,
		data: {},
		dataType: "json",
		success: function(book_list_result){
		},
	});
}
