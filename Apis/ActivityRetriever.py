from Apis.Amadeus.AmadeusClient import AmadeusClient
from Apis.Zomato.ZomatoClient import ZomatoClient
from Apis import APIConsts

CLIENTS = [AmadeusClient, ZomatoClient]


class ActivityRetriever(object):
    @classmethod
    def get_point_of_interest(cls, lat, long, end_time=None, radius=1, start_time=None):
        activites_to_return = {APIConsts.RETURN_LOCATION: []}
        for client in CLIENTS:
            activites_to_return[APIConsts.RETURN_LOCATION] += \
                client.get_point_of_interest(lat, long, end_time, radius, start_time)[APIConsts.RETURN_LOCATION]
        return activites_to_return
