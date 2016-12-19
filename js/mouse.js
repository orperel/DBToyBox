var mouse = angular.module('mouse', ['mouse.controllers', 'ngRoute']);

mouse.config(function ($routeProvider, $locationProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'views/mosaic.html',
            controller: 'mosaic'
        })
        .when('/city/', {
            templateUrl: 'views/city.html',
            controller: 'city'
        })
        .otherwise({
            redirectTo: '/'
        });
    $locationProvider.html5Mode(true);
});

angular.module('mouse.controllers', [])
    .controller('mosaic', function ($scope, $http) {
        $http.get('http://localhost:7000/api/mosaic/')
            .then(function (response) {
                console.log(response);
                $scope.mosaic = response.data;
            });
    })
    .controller('city', function ($scope, $http) {
        $http.get('http://localhost:7000/api/city/')
            .then(function (response) {
                console.log(response);
                $scope.data = response.data;
            });
    });