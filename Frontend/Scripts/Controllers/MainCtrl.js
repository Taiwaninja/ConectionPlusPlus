/**
 * Created by Noam on 3/30/2017.
 */
app.controller('mainCtrl', function($scope, $location){
    $scope.currentNavItem = 'page1';

    $scope.goto = function (url) {
        $location.path(url);
    }
});