function confirmReturnBook() {
	showConfirm("Return Book", "Are you sure you want to return a copy of this book?", function(){
		returnBook($("span#isbn").html());
	});
}

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
			
			if(bookData.available_copies>0){
				$("#status").html("Available");
				$("button#borrow-button").prop("disabled", false);
			}
			else{
				$("#status").html("Not Available");
				$("button#borrow-button").prop("disabled", true);
			}
			displaySuccessMessage(bookData.message);
		}
	});
}