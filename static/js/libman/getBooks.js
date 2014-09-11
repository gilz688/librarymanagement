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
				output+="<tr onClick='getSpecificBookInfo(\"" +books[i].ISBN+ "\");getBookAuthors(\"" +books[i].ISBN+ "\");'><td>"+ books[i].title+  "</td><td>" +books[i].ISBN+ "</td></tr>";
			}
			$("#library-name").html(libraryName);
			$("table#data-container").append(output);
		},
	});
}