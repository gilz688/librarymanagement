function getBookAuthors(ISBN){
	$.ajax({
		type: "get",
		url: local_site+ "getBookAuthors",
		data: {
			isbn: "0-07-013151-1"
		},
		dataType: "json",
		success: function(authors){
			var output= "";
			for(var i in authors)
			{
				output+= authors[i].lname+ ", " +authors[i].fname+ " " +authors[i].middle_initial +".";
				if((authors.length-1)>i)
					output+=", ";
			}
			$("#author").html(output);
		}
	});
}