function showConfirm(title, text, callback){
  $('#confirm').modal({
    show: true,
    backdrop: 'static',
    keyboard: false
  });
  $("#confirm-text").html(text);
  $("#confirm-title").html(title);
  $("#confirm-okBtn").off().on('click', callback);
}

function displayErrorMessage(text){
	setToastOption();
	toastr.error(text, "Error!");
	setToastMargin(0,10,6);
}

function displaySuccessMessage(text){
	setToastOption();
	toastr.success(text, "Success!");
	setToastMargin(0,10,6);
}

function setToastOption(){
	toastr.options = {
  		"closeButton": true,
  		"debug": false,
  		"positionClass": "toast-bottom-right",
  		"onclick": null,
  		"showDuration": "300",
  		"hideDuration": "1000",
  		"timeOut": "5000",
  		"extendedTimeOut": "1000",
  		"showEasing": "swing",
  		"hideEasing": "linear",
  		"showMethod": "fadeIn",
  		"hideMethod": "fadeOut"
	};
}

function setToastMargin(topM, left_rightM, bottomM){
	$("#toast-container>div").css('margin', topM+'px ' +left_rightM+'px ' +bottomM+'px');
}

function setToastWidth(toastWidth){
	$("#toast-container>div").width(toastWidth);
}

function displayPleaseFillDateErrorMessage() {
    setToastOption();
    toastr.error('Please enter the date', "Error!");
    setToastMargin(0,10,6);
}