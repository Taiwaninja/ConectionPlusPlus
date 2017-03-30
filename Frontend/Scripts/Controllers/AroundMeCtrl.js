/**
 * Created by Noam on 3/30/2017.
 */
app.controller('AroundMeCtrl', function ($scope, $http) {
    $scope.locations = null;

    $scope.init = function () {
        $.get("http://127.0.0.1:8080/api/get_mock")
            .done(function (data) {
                $scope.locations = JSON.parse(data);
            });
    }
});