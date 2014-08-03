var local_site= "http://localhost:8000/wlbc/default/";

$(document).ready(function(){
	viewBooks(1);
})

function viewBooks(libraryID){
	$.ajax({
		type: "post",
		url: local_site+ "viewBooks/" +libraryID,
		data: {
		},
		dataType: "json",
		success: function(books){
			var output= "<tr><th>Book Title</th></tr>";
			for(var i in books)
			{
				output+="<tr><td><a href='#' onClick='viewSpecificBook(" +books[i].ISBN+ ");'>"+ books[i].title+ "</a></td></tr>";
			}
			$("table#data-container").html(output);
			$("div#header").html("<h1>List of Books</h1>");
		},
	});
}