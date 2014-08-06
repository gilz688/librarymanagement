var local_site= "http://localhost:8000/librarymanagement/default/";

$(document).ready(function(){
	viewBooks("SCS");
})

function getBooks(libraryName){
	$.ajax({
		type: "post",
		url: local_site+ "getBooks/" +libraryName,
		data: {
		},
		dataType: "json",
		success: function(books){
			var output= "";
			for(var i in books)
			{
				output+="<tr><td onClick='getSpecificBook(" +books[i].ISBN+ ");getBookAuthors(" +books[i].ISBN+ ");'>"+ books[i].title+ "</td></tr>";
			}
			$("table#data-container").append(output);
		},
	});
}
