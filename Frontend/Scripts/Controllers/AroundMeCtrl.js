/**
 * Created by Noam on 3/30/2017.
 */
app.controller('AroundMeCtrl', function ($scope, $http) {
    $scope.locations = null;

    $scope.init = function () {
        $.get("http://10.10.192.137:8080/api/get_amadeus?longitude=32.0724416&latitude=34.7796856&radius=30")
            .done(function (data) {
                $scope.locations = JSON.parse(data);
            });
    }
});