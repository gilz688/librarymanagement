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
			$("#header").html("<h1>Most Borrowed Book For Year : " +year+ "<h1>");
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
			$("#header").html("<h1>Most Borrowed Book For : " +month + "-" + day + "-" + year+ "<h1>");
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
			$("#header").html("<h1>Most Borrowed Book For : " + month + "-" + year+ "<h1>");
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
			$("#header").html("<h1>Records For : " + day + "-" + month + "-" + year+ "<h1>");
			displayRecords(records);
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
			$("#header").html("<h1>Records For : " + month + "-" + year+ "<h1>");
			displayRecords(records);
		},
	});
}

function displayYearRecord(year, library) {
	$.ajax({
		type: "post",
		url: local_site+ "bookManagement/generateYearlyReport/",
		data: {
			year: year,
			lib_name: library
		},
		dataType: "json",
		success: function(records){
			$("#header").html("<h1>Records For Year : " + year+ "<h1>");
			displayRecords(records);
		},
	});
}


function displayMostBorrowedRecords(records){
	var output = "<table class=\"table table-bordered\"> <ul class=\"list-group\"> <li class=\"list-group-item\"><b>Title :</b> <span id=\"title\"></span></li> <li class=\"list-group-item\"><b>ISBN :</b> <span id=\"isbn\"></span></li> <li class=\"list-group-item\"><b>Library:</b> <span id=\"library\"></span></li> <li class=\"list-group-item\"><b>Total no. of transactions:</b> <span id=\"numtransacts\"></span></li> ";
	output += "</tbody></table></div></div>";
	$("#data-container").html(output);

	$("#title").html(records['title'])
	$("#isbn").html(records['ISBN']);
	$("#library").html(records['library']);
	$("#numtransacts").html(records['max_occur']);
}

function displayRecords(records) {
	var output = "<table> <tr> <td> <span id=\"isbnRecord\"> ISBN </span </td>  </tr> </table>";
	$("#data-container").html(output);
	for(var i in records) {
		//$("#data-container").html(records[i]['ISBN']);
		//\$("#data-container").html("Hello");
		$("#isbnRecord").html("Hello")
	}
}