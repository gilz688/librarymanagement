function getSpecificBook(ISBN){
	$("#bookInfo").modal("show");
	$.ajax({
		type: "post",
		url: local_site+ "getSpecificBookInfo/" + ISBN,
		data: {
			isbn: ISBN
		},
		dataType: "json",
		success: function(book){
			$("#isbn").html(book.ISBN);
			$("#myModalLabel").html(book.title);
			$("#publisher").html(book.publisher);
			$("#library").html(book.lib_name);
			if(book.available_copies>0)
				$("#status").html("Available");
			else
				$("#status").html("Not Available");
			$("#description").html(book.description);
		}
	});
}