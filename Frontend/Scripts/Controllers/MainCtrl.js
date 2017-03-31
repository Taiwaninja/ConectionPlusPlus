/**
 * Created by Noam on 3/30/2017.
 */
app.controller('mainCtrl', function ($scope, $location, $mdSidenav, $mdMedia){
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
});