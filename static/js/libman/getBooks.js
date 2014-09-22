function getBooks(libraryName){
	$.ajax({
		type: "post",
		url: local_site+ "viewBooks/getBooks/" + libraryName,
		data: {
		},
		dataType: "json",
		success: function(books){
			$("#library-name").html(libraryName);
			displayBooks(books);
			
		},
	});
}

function displayBooks(books){
	var output= "";
	for(var i in books){
		output+="<tr><td><a href=\"#\" onClick='getSpecificBookInfo(\"" +books[i].ISBN+ "\");getBookAuthors(\"" +books[i].ISBN+ "\");'>"+ books[i].title+  "</a></td><td>" +books[i].ISBN+ "</td></tr>";
	}
	$("table#data-container").append(output);
}