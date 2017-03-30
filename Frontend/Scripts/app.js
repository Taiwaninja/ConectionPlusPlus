/**
 * Created by Noam on 3/30/2017.
 */
var app = angular.module('ColHack', ['ngMaterial', 'ngRoute', 'ngMdIcons'])
    .config(function ($routeProvider, $locationProvider, $mdIconProvider, $mdThemingProvider) {
        $mdThemingProvider.theme('default')
            .primaryPalette('teal')
            .accentPalette('amber', {
                'default': '800'
            });

        $routeProvider
        .when('/home', {
            templateUrl: 'views/home.html',
            controller: 'mainCtrl'
        })
        .when('/flights', {
            templateUrl: 'views/flightSearch.html',
            controller: 'flightCtrl'
        })
        .when('/AroundMe', {
            templateUrl: 'views/aroundMe.html',
            controller: 'AroundMeCtrl'
        })
        .when('/Attractions', {
            templateUrl: 'views/placesSearch.html',
            controller: 'PlacesCtrl'
        })
        .otherwise({
            redirectTo: '/home'
        });
});