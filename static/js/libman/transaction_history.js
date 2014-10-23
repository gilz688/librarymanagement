function displayMostBorrowedBookYearly(year) {
	$.ajax({
		type: "post",
		url: local_site+ "bookManagement/getMostBorrowedBookPerYear/",
		data: {
			year: year,
			//library: library
		},
		dataType: "json",
		success: function(records){
			$("#panel_heading").html("Most Borrowed Book For Year : "+year);
			displayMostBorrowedRecords(records);
		},
	});
}

function displayMostBorrowedBookDaily(day, month, year) {
	$.ajax({
		type: "post",
		url: local_site+ "bookManagement/getMostBorrowedBookPerDay/",
		data: {
			day: day,
			month: month,
			year: year,
			//library: library
		},
		dataType: "json",
		success: function(records){
			$("#panel_heading").html("<h1>Most Borrowed Book For : " +month + "-" + day + "-" + year+ "<h1>");
			displayMostBorrowedRecords(records);
		},
	});
}

function displayMostBorrowedBookMonthly(month, year) {
	$.ajax({
		type: "post",
		url: local_site+ "bookManagement/getMostBorrowedBookPerMonth/",
		data: {
			month: month,
			year: year,
			//library: library
		},
		dataType: "json",
		success: function(records){
			$("#panel_heading").html("<h1>Most Borrowed Book For : " + month + "-" + year+ "<h1>");
			displayMostBorrowedRecords(records);
		},
	});
}

function displayDayRecord(day, month, year, library) {
	$.ajax({
		type: "post",
		url: local_site+ "bookManagement/getDayReport/",
		data: {
			day: day,
			month: month,
			year: year,
			library: library
		},
		dataType: "json",
		success: function(records){

			var recordsArray = [];
			for(var i = 0;i<records.length;i++){
				var rowInRecords = {
					title: records[i].book.title,
					isbn: records[i].book_manager.ISBN,
					libID: records[i].book_manager.librarian_id,
					date: records[i].book_manager.transact_date,
					time: records[i].book_manager.transact_time,
					type: records[i].book_manager.transact_type,
				}
				recordsArray.push(rowInRecords);
			}
			displayRecords(recordsArray,library);
		},
	});
}

function displayMonthRecord(month, year, library) {
	$.ajax({
		type: "post",
		url: local_site+ "bookManagement/generateMonthlyReport/",
		data: {
			month: month,
			year: year,
			lib_name: library
		},
		dataType: "json",
		success: function(records){
			var recordsArray = [];
			for(var i = 0;i<records.length;i++){
				var rowInRecords = {
					title: records[i].book.title,
					isbn: records[i].book_manager.ISBN,
					libID: records[i].book_manager.librarian_id,
					date: records[i].book_manager.transact_date,
					time: records[i].book_manager.transact_time,
					type: records[i].book_manager.transact_type,
				}
				recordsArray.push(rowInRecords);
			}
			displayRecords(recordsArray,library);
		},
	});
}

function displayYearRecord(year, library) {
	$.ajax({
		type: "post",
		url: local_site+ "bookManagement/generateYearlyReport",
		data: {
			year: year,
			lib_name: library,
		},
		dataType: "json",
		success: function(records){
			var recordsArray = [];
			for(var i = 0;i<records.length;i++){
				var rowInRecords = {
					title: records[i].book.title,
					isbn: records[i].book_manager.ISBN,
					libID: records[i].book_manager.librarian_id,
					date: records[i].book_manager.transact_date,
					time: records[i].book_manager.transact_time,
					type: records[i].book_manager.transact_type,
				}
				recordsArray.push(rowInRecords);
			}
			displayRecords(recordsArray,library);
		}
	});
}


function displayMostBorrowedRecords(records){
	var output = "<ul class='list-group'> <li class='list-group-item'><b>Title :</b> <span id='title'></span></li> <li class='list-group-item'><b>ISBN :</b> <span id='isbn'></span></li> <li class='list-group-item'><b>Library:</b> <span id='library'></span></li> <li class='list-group-item'><b>Total no. of transactions:</b> <span id='numtransacts'></span></li></ul>"
	
	$("#panel_body").html(output);

	$("#title").html(records['title'])
	$("#isbn").html(records['ISBN']);
	$("#library").html(records['library']);
	$("#numtransacts").html(records['max_occur']);
}

function displayRecords(records, library) {
	var output = '<div class="panel panel-info"><div id="panel_heading" class="panel-heading"></div><div id="panel_body" class="panel-body"><div class="table-responsive"><table id="history" class="table table-striped table-hover table-condensed" cellspacing="0" width="100%"><thead><tr><th>Title</th><th>ISBN</th><th>Librarian ID</th><th>Date</th><th>Time</th><th>Type</th></tr></thead></table></div></div></div></div>'
    $("#data-container").html(output);
    $("#panel_heading").html("<b>"+library+ " transaction history</b>");

    $('#history').DataTable( {
	    data: records,
	    columns: [
	    	{ data: 'title' },
	        { data: 'isbn' },
	        { data: 'libID' },
	        { data: 'date' },
	        { data: 'time' },
	        { data: 'type' }
	    ],
	    "columnDefs": [
		    { "width": "30%", "targets": 0 },
		    { "width": "15%", "targets": 1 },
		    { "width": "12%", "targets": 2 },
		    { "width": "12%", "targets": 3 },
		    { "width": "10%", "targets": 4 },
		    { "width": "5%", "targets": 5 },
		 ]
	});
}