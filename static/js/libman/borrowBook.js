function borrowBook(ISBN){
	$.ajax({
		type: "post",
		url: local_site+ "updateBook/borrowBook",
		dataType: 'json',
		data: {
			isbn: ISBN
		},
		success: function(book){
			$("span#availcopies").html(book.available_copies);
			if(book.available_copies == 0)
				$("button#borrow-button").prop("disabled", true);
			else
				$("button#borrow-button").prop("disabled", false);
			
			if(book.available_copies>0)
				$("#status").html("Available");
			else
				$("#status").html("Not Available");

			/*Temporary notification*/	
			alert(book.message);
		}

	});
}
