function borrowBook(ISBN){
	$.ajax({
		type: "post",
		url: local_site+ "updateBook/borrowBook",
		data: {
			isbn: ISBN
		},
		success: function(){
			getSpecificBookInfo(ISBN);
		}
	});
}
