/**
 * Created by Noam on 3/30/2017.
 */
app.controller('mainCtrl', function ($scope, $location, $mdSidenav, $mdMedia, $rootScope){
    $scope.currentNavItem = 'Home';

    $scope.goto = function (url, curr) {
        if (!$mdMedia('gt-sm'))
            $scope.toggleMenu('left');

        $location.path(url);
        $scope.currentNavItem = curr;
    }

    $scope.toggleMenu = function(componentId) {
        $mdSidenav(componentId).toggle();
    }

    $scope.submit = function (event) {
        if (event.keyCode == 13) {
            $location.path('/flights');
            $rootScope.$broadcast('on-search', { searchText: $scope.searchtxt });         
        }
    }
});