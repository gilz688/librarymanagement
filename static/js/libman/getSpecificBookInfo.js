function getSpecificBookInfo(ISBN){
	$("#bookInfo").modal("show");
	$.ajax({
		type: "post",
		url: local_site+ "viewBooks/getSpecificBookInfo",
		data: {
			isbn : ISBN
		},
		dataType: "json",
		success: function(book){
			$("#isbn").html(book.ISBN);
			$("#myModalLabel").html(book.title);
			$("#publisher").html(book.publisher);
			$("#author").html(book.author);
			$("#library").html(book.lib_name);
			$("#numcopies").html(book.no_of_copies);
            $("#availcopies").html(book.available_copies);
			$("#description").html(book.description);
			$("#book_pic").attr("src", local_site+ "viewBooks/download/" +book.pic);

			if(book.no_of_copies>book.available_copies)
				$("button#return-button").prop("disabled", false);
			else
				$("button#return-button").prop("disabled", true);
			if(book.available_copies>0){
				$("#status").html("Available");
				$("button#borrow-button").prop("disabled", false);
			}
			else{
				$("#status").html("Not Available");
				$("button#borrow-button").prop("disabled", true);
			}
		}
	});
}