function booksService($http, $q) {

    // Return public API.
    return ({
        getSpecificBookInfo: getSpecificBookInfo,
        getAllBooks: getAllBooks,
        searchBook: searchBook
    });

    // ---
    // PUBLIC METHODS.
    // ---
    function getSpecificBookInfo(ISBN) {
        var request = $http({
            method: "post",
            url: remote_site + "viewBooks/getBookInfo",
            data: {
                isbn: ISBN
            },
            headers: {
                'Content-type': 'application/json'
            }
        });

        return (request.then(handleSuccess, handleError));
    }

    function getAllBooks(start,end) {
        var request = $http({
            method: "get",
            url: remote_site + "viewBooks/getAllBooks?start="+start+"&end="+end,
        });
        return (request.then(handleSuccess, handleError));
    }


    function searchBook(key,start,end){
            var request = $http({
                method: "get",
                url: remote_site + "searchBook/searchAllBook/?keyword="+key+"&start="+start+"&end="+end,
            });
        return (request.then(handleSuccess, handleError));
    }

    // ---
    // PRIVATE METHODS.
    // ---
    function handleError(response) {
        if (!angular.isObject(response.data) ||
            !response.data.message
        ) {
            return ($q.reject("An unknown error occurred."));
        }
        return ($q.reject(response.data.message));
    }

    function handleSuccess(response) {
        console.dir(response.data);
        return (response.data);
    }
}
