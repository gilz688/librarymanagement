function searchBookByAuthor(author){
	$.ajax({
		type: "post",
		url: local_site+ "searchBook/searchByAuthor/",
		data: {
			"author" : author,
		},
		dataType: "json",
		success: function(books){
			var output= "";
			for(var i in books)
			{
				output+="<tr onClick='getSpecificBookInfo(\"" +books[i].ISBN+ "\");getBookAuthors(\"" +books[i].ISBN+ "\");'><td>"+ books[i].title+  "</td><td>" +books[i].ISBN+ "</td></tr>";
			}
			$("table#data-container").append(output);
		},
		error: function(e){
			
		}
	});
}