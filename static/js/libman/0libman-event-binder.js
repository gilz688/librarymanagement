var local_site= "http://127.0.0.1:8000/librarymanagement/";
$(document).ready(function(){
	getBooks("COE-Library");
	
	/*binds the 'addAvailableCopies' function when the user clicks the 'Return' button*/
	$("button#return-button").click(function(){
		addAvailableCopies($("span#isbn").html());
	});

    $("button#borrow-button").click(function() {
        borrowBookJS();
    });

    function borrowBookJS() {
        if(confirm("Are you sure you want to borrow a copy of this book?")) {
            borrowBook($("span#isbn").html());
        }
        else {
            return false;
        }
    }


	/*clears the modal data when the closes the modal*/
	$('#bookInfo').on('hidden.bs.modal', function () {
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
	})
})