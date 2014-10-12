function getBookInfo(ISBN){
	$("#bookInfo").modal("show");
	$.ajax({
		type: "post",
		url: local_site+ "viewBooks/getBookInfo",
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
			$("#location").html(book.library.address);
			$("#numcopies").html(book.no_of_copies);
            $("#availcopies").html(book.available_copies);
			$("#description").html(book.description);
			$("#book_pic").attr("src", local_site+ "viewBooks/download/" +book.pic);

			if(book.available_copies>0)
				$("#status").html("Available");
			else
				$("#status").html("Not Available");

			var output = "";
			for(var i in book.authors){
				output+= book.authors[i].lname+ ", " +book.authors[i].fname+ " " +book.authors[i].middle_initial +".";
				if((book.authors.length-1)>i)
					output+="; ";
			}
			$("#author").html(output);

			checkIfLibrarian(book.lib_name,book.no_of_copies,book.available_copies);
		}
	});
}

function checkIfLibrarian(libraryName,numCopies,availCopies){
	$.ajax({
		type: "post",
		url: local_site+ "auth/getSession",
		dataType: "json",
		success: function(result){
			if(result != null){
				if(result.lib_name == libraryName){
					displayBorrowReturnButton(numCopies,availCopies);
				}
			}
		}
	});
}

function displayBorrowReturnButton(numOfCopies,availableCopes){
	var buttons = "<button id=\"borrow-button\" onclick='confirmBorrowBook();' class=\"btn btn-primary\" >Borrow</button>";
	buttons += "<button id=\"return-button\" onclick='confirmReturnBook();' class=\"btn btn-primary\" >Return</button>";
	$("#borrow-return-button").html(buttons);

	if(numOfCopies>availableCopes){
		$("#return-button").prop("disabled", false);
	}
	else{
		$("#return-button").prop("disabled", true);
	}

	if(availableCopes>0){
		$("#borrow-button").prop("disabled", false);
	}
	else{
		$("#borrow-button").prop("disabled", true);
	}
	
}