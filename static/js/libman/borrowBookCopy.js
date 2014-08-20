function borrowBookCopy(ISBN){
	$.ajax({
		type: "post",
		url: local_site+ "updateBook/borrowBookCopy",
		data: {
			isbn: ISBN
		},
		success: function(){
			getSpecificBookInfo(ISBN);
		}
	});
}
