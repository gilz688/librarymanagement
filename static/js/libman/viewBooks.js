var local_site= "https://localhost:8000/wlbc/default/";

$(document).ready(function(){
	viewBooks("SCS");
})

function viewBooks(libraryName){
	$.ajax({
		type: "post",
		url: local_site+ "viewBooks/" +libraryName,
		data: {
		},
		dataType: "json",
		success: function(books){
			var output= "";
			for(var i in books)
			{
				output+="<tr><td><a href='#' onClick='viewSpecificBook(" +books[i].ISBN+ ");'>"+ books[i].title+ "</a></td></tr>";
			}
			$("table#data-container").html(output);
			$("div#header").html("<h1>List of Books</h1>");
		},
	});
}
