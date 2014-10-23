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
			displayBooks(books,libraryName);
		},
	});
}

function displayBooks(books,libraryName){

	var recordsArray = [];
	for(var i in books){
		var rowInRecords = {
			title: '<a href="#" onClick="getBookInfo(\''+books[i].ISBN+'\');">'+ books[i].title+ '</a>',
			isbn: books[i].ISBN,
		}
		recordsArray.push(rowInRecords);
	}

	var output = '<div class="panel panel-info"><div id="panel_heading" class="panel-heading"></div><div class="panel-body"><div class="table-responsive"><table id="history" class="table table-striped table-hover table-condensed" cellspacing="0" width="100%"><thead><tr><th>Title</th><th>ISBN</th></tr></thead></table></div></div></div></div>'
    $("#data-container").html(output);
    $("#panel_heading").html("<b>"+libraryName+ " transaction history</b>");

    $('#history').DataTable( {
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
}

function displaySearchedBooks(books,keyword){

	
	
	var recordsArray = [];
	
	for(var i in books){
		var rowInRecords = {
			title: '<a href="#" onClick="getBookInfo(\''+books[i].ISBN+'\');">'+ books[i].title+ '</a>',
			isbn: books[i].ISBN,
		}
		recordsArray.push(rowInRecords);
	}
	
	var output = '<div class="panel panel-info"><div id="panel_heading" class="panel-heading"></div><div class="panel-body"><div class="table-responsive"><table id="history" class="table table-striped table-hover table-condensed" cellspacing="0" width="100%"><thead><tr><th>Title</th><th>ISBN</th></tr></thead></table></div></div></div></div>'
    $("#data-container").html(output);
    $("#panel_heading").html("<b>Search results for '" + keyword + "'</b>");
    $('#history').DataTable( {
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
}