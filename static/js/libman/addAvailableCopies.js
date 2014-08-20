function addAvailableCopies(ISBN){
	$.ajax({
		type: "post",
		url: local_site+ "updateBook/addAvailableCopies",
		data: {
			isbn: ISBN
		},
		success: function(){
			getSpecificBookInfo(ISBN);
		}
	});
}