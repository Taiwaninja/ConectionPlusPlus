import json
from Apis.ActivityRetriever import ActivityRetriever
from datetime import datetime

# coordinates might be upside down

CONNECTION1 = {"lat": 50.038952, "long": 8.561991, "radius": 100,
               "start_time": datetime(year=2017, month=4, day=11, hour=4, minute=50),
               "end_time": datetime(year=2017, month=4, day=11, hour=21, minute=0)}

CONNECTION2 = {"lat": 48.116428, "long": 16.565652, "radius": 100,
               "start_time": datetime(year=2017, month=4, day=20, hour=23, minute=45),
               "end_time": datetime(year=2017, month=4, day=21, hour=20, minute=25)}


def main():
    connection1_activities = ActivityRetriever.get_point_of_interest(**CONNECTION1)
    with open("./DataSamples/Activity1.json", "wb") as conn1_file:
        json.dump(connection1_activities, conn1_file, indent=4)
        # connection2_activities = ActivityRetriever.get_point_of_interest(**CONNECTION2)
        # with open("./DataSamples/Activity2.json", "w") as conn1_file:
    connection2_activities = ActivityRetriever.get_point_of_interest(**CONNECTION2)
    with open("./DataSamples/Activity2.json", "wb") as conn2_file:
        json.dump(connection2_activities, conn2_file, indent=4)
        # connection2_activities = ActivityRetriever.get_point_of_interest(**CONNECTION2)
        # with open("./DataSamples/Activity2.json", "w") as conn1_file:


#        json.dump(conn1_file, indent=4)


if __name__ == "__main__":
    main()
