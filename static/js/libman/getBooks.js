function getBooks(libraryName){
	$.ajax({
		type: "post",
		url: local_site+ "viewBooks/getBooks/" + libraryName,
		data: {
		},
		dataType: "json",
		success: function(books){
			$("#header").html("<h1>Home Library: " +libraryName+ "<h1>");
			displayBooks(books);
		},
	});
}

function displayBooks(books){
	var output = "<table class=\"table table-bordered\">";
	output += "<thead>";
	output += "<tr><th style=\"text-align:center\">Book Title</th><th style=\"text-align:center\">ISBN</th></tr>";
	output += "</thead><tbody>"; 
	for(var i in books){
		output +="<tr><td><a href=\"#\" onClick='getBookInfo(\"" +books[i].ISBN+ "\");'>"+ books[i].title+  "</a></td><td>" +books[i].ISBN+ "</td></tr>";
	}
	output += "</tbody></table></div></div>";
	$("#data-container").html(output);
}