function booksController($scope, $q, booksService) {
    $scope.ready = true;

    ons.ready(function() {
        viewBooks();
    });

    // bind function to html element with ng-click="viewSpecificBookInfo"
    $scope.viewSpecificBookInfo = viewSpecificBookDetails;
    $scope.searchBook = searchAllBook;
    $scope.baseUrl = remote_site;
    $scope.viewBooks = viewBooks;

    function setBusy(busy){
        $scope.ready = !busy;
    }

    function viewBooks() {
        nullResults = false;
        $scope.books = [];
        addBooks(0, 4);
        bindViewBooksToNextPage();
    }

    function bindViewBooksToNextPage(){
        $scope.nextPage = function() {
            addBooks($scope.books.length, $scope.books.length + 1);
        }
    }

    function addBooks(start, end) {
        if ($scope.ready){
            setBusy(true);
            booksService.getAllBooks(start, end).then(
                function(books) {

                    console.dir(books);
                    for (var i = 0; i < books.length; i++) {
                        $scope.books.push(books[i]);
                    }

                    setBusy(false);
                }
            );
        }
    }

    function setBooks(aBooks) {
        $scope.books = aBooks;
    }

    function viewSpecificBookDetails(isbn) {
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


    function searchAllBook(keyword) {
        $scope.books = [];
        if (keyword == "") {
            viewBooks();
        } else {
            booksService.searchBook(keyword).then(
                function(books) {
                    setBooks(books);
                }
            );
        }
    }



    function searchAllBook(keyword) {
        $scope.books = [];
        searchAddBook(keyword, 0, 4);
        bindSearchBookToNextPage(keyword);
    }

    function searchAddBook(keyword,start, end) {
        if ($scope.ready){
            setBusy(true);
            booksService.searchBook(keyword,start, end).then(
                function(books) {

                    console.dir(books);
                    for (var i = 0; i < books.length; i++) {
                        $scope.books.push(books[i]);
                    }

                    $scope.nullResults = $scope.books.length == 0;
                    setBusy(false);
                }
            );
        }
    }

     function bindSearchBookToNextPage(keyword){
        $scope.nextPage = function() {
            searchAddBook(keyword, $scope.books.length, $scope.books.length + 1);
        }
    }

}
