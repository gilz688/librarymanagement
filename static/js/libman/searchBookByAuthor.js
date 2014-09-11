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
				output+="<tr><td onClick='getSpecificBookInfo(\"" +books[i].ISBN+ "\");getBookAuthors(\"" +books[i].ISBN+ "\");'>"+ books[i].title+  "</td></tr>";
			}
			$("table#data-container").append(output);
		},
		error: function(e){
			
		}
	});
}