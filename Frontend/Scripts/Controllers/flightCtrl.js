/**
 * Created by Noam on 3/30/2017.
 */
app.controller('flightCtrl', function ($scope) {
    $scope.flights = null;
    $scope.nonstop = [];
    $scope.layover = [];
    $scope.departure = "TLV";
    $scope.destination = "LON";
    $scope.startDate;
    $scope.endDate;
    $scope.travelers = 1;
    $scope.attractions = [];
    $scope.currLayover = null;

    $scope.init = function () {
        $.get("http://10.10.192.137:8080/api/get_flights")
            .done(function (data) {
                $scope.flights = (JSON.parse(data)).Flights;
                var minCost = 0;
                for (var i = 0; i < $scope.flights.length; i++) {
                    if ($scope.flights[i].Layover == 0)
                        $scope.nonstop.push($scope.flights[i]);
                    else {
                        function get_data_func(i) {
                            return function (data) {
                                $scope.flights[i].Activities.push({
                                    locations: JSON.parse(data)
                                });

                                if ($scope.layover[0] == null)
                                    $scope.currLayover = $scope.flights[i];

                                $scope.layover.push($scope.flights[i]);

                                if ($scope.flights[i].price < $scope.currLayover.price)
                                    $scope.currLayover = $scope.flights[i];
                            };
                        };

                        $.get("http://10.10.192.137:8080/api/get_amadeus?longitude=" + $scope.flights[i].arrival1.Location.lng + "&deal_id=" + $scope.flights[i].deal_id +"&latitude=" + $scope.flights[i].arrival1.Location.lat + " & radius=30")
                            .done(
                            get_data_func(i)
                            );
                    }
                }
                console.log('test');
            });        
    };
});