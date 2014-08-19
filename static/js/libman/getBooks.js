function getBooks(libraryName){
	$.ajax({
		type: "post",
		url: local_site+ "viewBooks/getBooks/" + libraryName,
		data: {
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
	});
}
