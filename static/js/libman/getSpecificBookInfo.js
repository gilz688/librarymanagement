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
			checkIfLibrarian(book.lib_name);
		}
	});
}


function checkIfLibrarian(libraryName){
	$.ajax({
		type: "post",
		url: local_site+ "auth/getSession",
		dataType: "json",
		success: function(result){
			if(result != null){
				if(result.lib_name == libraryName){
					displayBorrowReturnButton();
				}
				else
					$("#borrow-return-button").html("");
			}
			else
				$("#borrow-return-button").html("");
		}
	});
}

function displayBorrowReturnButton(){
	var buttons = "<button id=\"borrow-button\" onclick='borrowBookJS();' class=\"btn btn-primary\" style=\"margin: 0 5px;\">Borrow</button>";
	buttons += "<button id=\"return-button\" onclick='returnBookJS();' class=\"btn btn-primary\" style=\"margin: 0 5px;\">Return</button>";
	$("#borrow-return-button").html(buttons);
}