function booksService($http, $q) {

    // Return public API.
    return ({
        getSpecificBookInfo: getSpecificBookInfo,
        getBookAuthors: getBookAuthors,
        getAllBooks: getAllBooks
    });

    // ---
    // PUBLIC METHODS.
    // ---
    function getSpecificBookInfo(ISBN) {
        var request = $http({
            method: "post",
            url: remote_site + "viewBooks/getSpecificBookInfo",
            data: {
                isbn: ISBN
            },
            headers: {
                'Content-type': 'application/json'
            }
        });
        return (request.then(handleSuccess, handleError));
    }

    function getAllBooks() {
        var request = $http({
            method: "get",
            url: remote_site + "viewBooks/getAllBooks/",
        });
        return (request.then(handleSuccess, handleError));
    }

    function getBookAuthors(ISBN) {
        var request = $http({
            method: "post",
            url: remote_site + "viewBooks/getBookAuthors",
            data: {
                isbn: ISBN
            },
            headers: {
                'Content-type': 'application/json'
            }
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
