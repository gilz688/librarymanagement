function booksController($scope, $q, booksService) {
    viewBooks("COE-Library");

    $scope.baseUrl = remote_site;
    
    $scope.viewBooks = function(){
        $scope.books = [];
        viewBooks("COE-Library");
        var options = {
            animation: 'none', // What animation to use
            onTransitionEnd: function() {} // Called when finishing transition animation
        };
        tabbar.pushPage("home.html", options);
    };

    // bind function to html element with ng-click="viewSpecificBookInfo"
    $scope.viewSpecificBookInfo = viewSpecificBookDetails;

    function viewBooks(library) {
        booksService.getBooks(library).then(
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
            	getCurrentBookAuthors();
                var options = {
                    animation: 'slide', // What animation to use
                    onTransitionEnd: function() {} // Called when finishing transition animation
                };
                mainnav.pushPage("book_details.html", options);
            }
        );
    }

    function getCurrentBookAuthors() {
        booksService.getBookAuthors($scope.currentBook.isbn).then(
            function(authors) {
                for(var i in authors){
            		$scope.currentBook.authorsTxt += (authors[i].lname + ", " + authors[i].fname + " " + authors[i].middle_initial + "; "); 
            	}
            }
        );
    }
}
