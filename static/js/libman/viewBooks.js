var local_site= "http://localhost:8000/librarymanagement/default/";

$(document).ready(function(){
	viewBooks("scs_lib");
})

function viewBooks(libraryName){
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
				output+="<tr><td onClick='viewSpecificBook(" +books[i].ISBN+ ");'>"+ books[i].title+ "</td></tr>";
			}
			$("table#data-container").append(output);
		},
	});
}
