function returnBook(ISBN){
	$.ajax({
		type: "post",
		url: local_site+ "updateBook/returnBook",
		data: {
			isbn: ISBN
		},
		dataType: "json",
		success: function(bookData){
			$("span#availcopies").html(bookData.available_copies);
			if(bookData.num_of_copies>bookData.available_copies)
				$("button#return-button").prop("disabled", false);
			else
				$("button#return-button").prop("disabled", true);
			
			if(bookData.available_copies>0)
				$("#status").html("Available");
			else
				$("#status").html("Not Available");

			/*Temporary notification*/	
			alert(bookData.message);
		}
	});
}