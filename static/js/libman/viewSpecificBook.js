function viewSpecificBook(ISBN){
	$("#bookInfo").modal();
	$.ajax({
		type: "post",
		url: local_site+ "viewSpecificBook/" + ISBN,
		data: {
			isbn: ISBN
		},
		dataType: "json",
		success: function(book){
			$("#isbn").html(book.isbn);
			$("#bookTitle").html(book.title);
			$("#publisher").html(book.publisher);
			$("#author").html(book.author);
			$("#location").html(book.location);
			$("#description").html(book.description);
		}
	});
}