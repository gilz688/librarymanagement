
//var local_site= "http://127.0.0.1:8000/librarymanagement/viewBooks/";

function getBookAuthors(ISBN){
	$.ajax({
		type: "post",
		url: local_site+ "getBookAuthors/" + ISBN,
		data: {
			isbn: ISBN
		},
		dataType: "json",
		success: function(authors){
			var output= "";
			for(var i in authors)
			{
				output+= authors[i].lname+ ", " +authors[i].fname+ " " +authors[i].middle_initial +".";
				if((authors.length-1)>i)
					output+="; ";
			}
			$("#author").html(output);
		}
	});
}