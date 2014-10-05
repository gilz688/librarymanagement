function confirmBorrowBook() {
    showConfirm("Borrow Book", "Are you sure you want to borrow a copy of this book?", function(){
    	borrowBook($("span#isbn").html());
    });
}

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
			
			if(book.available_copies>0) {
				$("#status").html("Available");
				$("button#borrow-button").prop("disabled", false);
				$("button#return-button").prop("disabled", false);
			}
			else {
				$("#status").html("Not Available");
				$("button#borrow-button").prop("disabled", true);
				$("button#return-button").prop("disabled", false);
			}
			displaySuccessMessage(book.message);
		}

	});
}
