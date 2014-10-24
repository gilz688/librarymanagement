function getBooks(libraryName){
	$.ajax({
		type: "post",
		url: local_site+ "viewBooks/getBooks/" + libraryName,
		data: {
		},
		dataType: "json",
		success: function(books){
			$("#header").html("<h1>Home Library: " +libraryName+ "<h1>");
			$("#panel_heading").html("<b>"+libraryName+" books</b>");
			displayBooks(books);
		},
	});
}

function displayBooks(books){
	var recordsArray = [];
	for(var i in books){
		var rowInRecords = {
			title: '<a href="#" onClick="getBookInfo(\''+books[i].ISBN+'\');">'+ books[i].title+ '</a>',
			isbn: books[i].ISBN,
		};
		recordsArray.push(rowInRecords);
	}	
	var output = '<table id="book_data" class="table table-striped table-hover table-condensed" cellspacing="0" width="100%"><thead><tr><th>Title</th><th>ISBN</th></tr></thead></table>';
    $("#panel_body").html(output);
    $('#book_data').DataTable( {
    	//"bFilter": false,
	    data: recordsArray,
	    columns: [
	    	{ data: 'title' },
	        { data: 'isbn' },
	    ],
	    "columnDefs": [
		    { "width": "30%", "targets": 0 },
		    { "width": "15%", "targets": 1 },
		 ]
	});
	//$("#data-container").show();
}