$(document).ready(function() {
    viewHome();

    $("#borrowListData").hide();
    $("#historyListData").hide();
    $('#historyList').hide();

    $("#borrowList").click(viewBorrowOption);
    $("#historyList").click(viewHistoryOption);


    $("#home").click(viewHome);

    $("#session").click(signInOrSignOut);
    $("#submitLogIn").click(logInUser);

    $("#search-input").keypress(checkKey);
    $("#search-button").click(searchBook);

    $(".mode-menu").click(setSearchMode);

    $("#logInModal").on('hidden.bs.modal', clearLoginModal);
    $("#bookInfo").on('hidden.bs.modal', clearBookModal);

    $('#borrowButtonD').click(viewMostBorrowedBooks);
    $('#borrowButtonM').click(viewMostBorrowedBooks);
    $('#borrowButtonY').click(viewMostBorrowedBooks);

    $('#historyButtonD').click(viewTransactionHistory);
    $('#historyButtonM').click(viewTransactionHistory);
    $('#historyButtonY').click(viewTransactionHistory);

    setCurrentDate();
    $("#borDay").click(setCurrentDate);
    $("#borYear").click(setCurrentDate);
    $("#histDay").click(setCurrentDate);

    setCurrentMonth();
    $("#borMonth").click(setCurrentMonth);
    $("#histMonth").click(setCurrentMonth);

    setCurrentYear();
    $("#borYear").click(setCurrentMonth);
    $("#histYear").click(setCurrentMonth);   
});

function setCurrentDate() {
    dateFormat();
    $('#borDayInput').val(new Date().toDateInputValue());
    $("#histInputD").val(new Date().toDateInputValue());
}

function setCurrentMonth() {
    var d = new Date();
    var year = d.getYear() + 1900;
    var month = (d.getMonth() + 1).toString();
    if(month.length == 1)
    	month = "0" + month
    $('#borMonthInput').val(year.toString() + '-' + month);
    $("#histInputM").val(year.toString() + '-' + month);
}

function setCurrentYear() {
    var d = new Date();
    var year = d.getYear() + 1900;
    $('#borYearInput').val(year.toString());
    $("#histInputY").val(year.toString());
}

function dateFormat() {
    Date.prototype.toDateInputValue = (function() {
        var local = new Date(this);
        local.setMinutes(this.getMinutes() - this.getTimezoneOffset());
        return local.toJSON().slice(0, 10);
    });
}

function viewMostBorrowedBooks() {
    var data = $(this).parent().serializeArray();

    if (data[0].value == '')
        displayPleaseFillDateErrorMessage();
    else if (data[0].name == 'bdate') {
        date = data[0].value.split("-");
        year = date[0];
        month = date[1];
        day = date[2];
        displayMostBorrowedBookDaily(day, month, year);
    } else if (data[0].name == 'bmonth') {
        date = data[0].value.split("-");
        year = date[0];
        month = date[1];
        day = date[2];
        displayMostBorrowedBookMonthly(month, year);
    } else if (data[0].name == 'byear') {
        year = data[0].value;
        displayMostBorrowedBookYearly(year);
    }
}

function viewTransactionHistory() {
    var data = $(this).parent().serializeArray();

    if (data[0].value == '')
        displayPleaseFillDateErrorMessage();
    else if (data[0].name == 'hdate') {
        date = data[0].value.split("-");
        year = date[0];
        month = date[1];
        day = date[2];
        library = data[1].value;
        displayDayRecord(day, month, year, library);
    } else if (data[0].name == 'hmonth') {
        date = data[0].value.split("-");
        year = date[0];
        month = date[1];
        library = data[1].value;
        displayMonthRecord(month, year, library);
    } else if (data[0].name == 'hyear') {
        year = data[0].value;
        library = data[1].value;
        displayYearRecord(year, library);
    }
}

function viewBorrowOption() {
    if ($("#borrowListData").is(':visible'))
        $("#borrowListData").hide('slow');
    else
        $("#borrowListData").show('slow');

    $("#historyListData").hide('slow');
}

function viewHistoryOption() {
    if ($("#historyListData").is(':visible'))
        $("#historyListData").hide('slow');
    else
        $("#historyListData").show('slow');

    $("#borrowListData").hide('slow');
}

function viewHome() {
    $.ajax({
        type: "post",
        url: local_site + "auth/getSession",
        dataType: "json",
        success: function(result) {
            if (result != null) {
                viewLibrarianHome(result.lib_name);
            } else {
                viewUserHome();
            }
        }
    });
}

function viewLibrarianHome(libraryName) {
    getBooks(libraryName);
    viewGenerateReportOptionsLoggedIn();
    $("#session a").html("Log Out");
    hideBookManagementOption();
}

function viewUserHome() {
    $("#session a").html("Log In");
    $("#header").html("");
    $("#panel_body").html("<center><h4>Welcome to Librarymanagement<h4></center>");
    $("#panel_heading").html("");
    //$("#data-container").hide();
    viewGenerateReportOptionsNotLoggedIn();
}


function viewGenerateReportOptionsNotLoggedIn() {
    $('#historyList').hide();
}

function viewGenerateReportOptionsLoggedIn() {
    $('#historyList').slideDown('slow');
}

function signInOrSignOut() {
    var session = $("#session a").html();

    if (session == "Log In") {
        $("#logInModal").modal('show');
    } else {
        logOutUser();
        hideBookManagementOption();
    }
}


function checkKey(e) {
    e.which
    var key = e.which;
    if (key == 13) // the enter key code
    {
        searchBook();
        return false;
    }
}

function setSearchMode() {
    var mode = $(this).children().first().html();
    $("#mode-selected").val(mode);
    $("#mode-selected b").html(mode);
}


function clearLoginModal() {
    $("#username").val("");
    $("#password").val("");
    $("#sign-in-error").html("");
}

function clearBookModal() {
    $("#isbn").html("");
    $("#myModalLabel").html("");
    $("#publisher").html("");
    $("#author").html("");
    $("#library").html("");
    $("#numcopies").html("");
    $("#status").html("");
    $("#availcopies").html("");
    $("#description").html("");
    $("#book_pic").attr("src", "#");
    $("#borrow-return-button").html("");
}

function hideBookManagementOption() {
    $("#borrowListData").hide();
    $("#historyListData").hide();
}
