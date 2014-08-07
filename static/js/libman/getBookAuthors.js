function getBookAuthors(ISBN){
	$.ajax({
		type: "post",
		url: local_site+ "getBookAuthors/" + ISBN,
		data: {
		},
		dataType: "json",
		success: function(authors){
			var output= "";
			for(var i in authors)
			{
				output+= authors[i].fname+ " " +authors[i].lname;
				if((authors.length-1)>i)
					output+=", ";
			}
			$("#author").html(output);
		}
	});
}