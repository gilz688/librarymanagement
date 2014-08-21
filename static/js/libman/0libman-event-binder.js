var local_site= "http://127.0.0.1:8000/librarymanagement/";
$(document).ready(function(){
	
	getBooks("COE-Library");
	
	/*binds the 'borrowBookJS' function when the user clicks the 'Borrow' button*/
	$("button#borrow-button").click(borrowBookJS);

	/*binds the 'returnBookJS' function when the user clicks the 'Return' button*/
	$("button#return-button").click(returnBookJS);
	
	/*binds the clearModal function when the user closes the modal*/
	$("#bookInfo").on('hidden.bs.modal', clearModal);
});



function borrowBookJS() {
    if(confirm("Are you sure you want to borrow a copy of this book?")) {
        borrowBook($("span#isbn").html());
    }
    else {
        return false;
    }
}

function returnBookJS() {
    if(confirm("Are you sure you want to return a copy of this book?")) {
        returnBook($("span#isbn").html());
    }
    else {
        return false;
    }
}

function clearModal() {
	$("#isbn").html("");
	$("#myModalLabel").html("");
	$("#publisher").html("");
	$("#author").html("");
	$("#library").html("");
	$("#numcopies").html("");
	$("#status").html("");
	$("#availcopies").html("");
	$("#description").html("");
	$("#book_pic").attr("src", "#");
	$("button#return-button").prop("disabled", true);
	$("button#borrow-button").prop("disabled", true);
}