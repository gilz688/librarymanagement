function getSpecificBook(ISBN){
	$("#bookInfo").modal("show");
	$.ajax({
		type: "get",
		url: local_site+ "getSpecificBookInfo",
		data: {
			isbn: "0-07-013151-1"
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
			$("#book_pic").attr("src", local_site+ "download/" +book.pic);
		}
	});
}