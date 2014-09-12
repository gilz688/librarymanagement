function searchBookByISBN(isbn){
	$.ajax({
		url: local_site+ "searchBook/searchByISBN/" + isbn,
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
		error: function(e, status, error){
			if(results == 0){
				displayErrorMessage("No Book Found");
			}
		}
	});
}
