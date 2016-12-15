angular.module('mouse', ['mouse.controllers']);

angular.module('mouse.controllers', [])
    .controller('events', function ($scope, $http) {
        $http.get('http://localhost:7000/mosaic/')
            .then(function (response) {
                console.log(response);
                $scope.mosaic = response.data;
            });
    });