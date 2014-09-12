function searchBookByTitle(book_title){
	$.ajax({
		type: "post",
		url: local_site+ "searchBook/searchBookByTitle/",
		data: {
			"keyword" : book_title,
		},
		dataType: "json",
		success: function(books){
			var output= "";
			for(var i in books)
			{
				results++;
				output+="<tr onClick='getSpecificBookInfo(\"" +books[i].ISBN+ "\");getBookAuthors(\"" +books[i].ISBN+ "\");'><td>"+ books[i].title+  "</td><td>" +books[i].ISBN+ "</td></tr>";
			}
			$("table#data-container").append(output);
		},
		error: function(e){
			if(results == 0){
				displayErrorMessage("Not found!");
			}
		}
	});
}
