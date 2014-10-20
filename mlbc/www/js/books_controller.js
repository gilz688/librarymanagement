function booksController($scope, $q, booksService) {
    $scope.books = [];
    addBooks(1,3);

    $scope.baseUrl = remote_site;
    
    $scope.viewBooks = function(){
        $scope.books = [];
        addBooks(1,3);
    };

    $scope.nextPage = function(){
        addBooks($scope.books.length,$scope.books.length+1);
    }

    // bind function to html element with ng-click="viewSpecificBookInfo"
    $scope.viewSpecificBookInfo = viewSpecificBookDetails;

    $scope.searchBook = searchAllBook;

    function addBooks(start,end) {
        booksService.getAllBooks(start,end).then(
            function(books) {
                console.dir(books);
                for(var i=0;i<books.length;i++){
                    $scope.books.push(books[i]);
                }
            }
        );
    }

    function setBooks(aBooks) {
        $scope.books = aBooks;
    }

    function viewSpecificBookDetails(isbn){
    	booksService.getSpecificBookInfo(isbn).then(
            function(book) {
            	$scope.currentBook = book;
                var options = {
                    animation: 'slide', // What animation to use
                    onTransitionEnd: function() {} // Called when finishing transition animation
                };
                mainnav.pushPage("book_details.html", options);
            }
        );
    }


    function searchAllBook(keyword){
        $scope.books = [];
        if (keyword == ""){
            viewBooks();
        }
        else{
            booksService.searchBook(keyword).then(
                function(books){
                    setBooks(books);
                }
            );
        }
    }
	
	$scope.twoPlusThree = function() {
		return 2 + 3;
	}

}
