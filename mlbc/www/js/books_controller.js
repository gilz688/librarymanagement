function booksController($scope, $q, booksService) {
    viewBooks();

    $scope.baseUrl = remote_site;
    
    $scope.viewBooks = function(){
        $scope.books = [];
        viewBooks();
    };

    // bind function to html element with ng-click="viewSpecificBookInfo"
    $scope.viewSpecificBookInfo = viewSpecificBookDetails;

    function viewBooks() {
        booksService.getAllBooks().then(
            function(books) {
                setBooks(books);
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

}
