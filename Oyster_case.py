#!/usr/bin/env python
# coding: utf-8


class StationandFare(object):
    #this class contains station names and the zone in which they are in
    
    STATIONS = {
        "Holborn":[1],
        "Aldgate":[1],
        "Earl's Court":[1,2],
        "Hammersmith":[2],
        "Arsenal":[2],
        "Wimbledon":[3]
    }
    
    #max fare and other fare variables according to zones and journey type
    max_fare = 3.20
    bus_fare = 1.8
    zone_one_fare = 2.50
    one_zone_outside_zone1_fare = 2.00
    two_zone_with_zone1_fare = 3.00
    two_zone_without_zone1_fare = 2.25
    more_than_two_zones = 3.20
          
    #function to get stations'zone info    
    def get_station_info(self,name):
        #checking if the station do exists
        if name in self.STATIONS.keys():
            zone = self.STATIONS[name]
            return zone
        else:
            print("The station {} can be reached by bus as it is not in the tube stations list".format(name))


class Journey(object):
    #class for journey realted info and calculating cost by journey and its type
    
    #initialising journey type class variable for this class
    jrny_type = 'bus'
    
    def __init__(self):
        self.journey = {'start':None,"end":None}
        self._sf = StationandFare()
    
    #setting the starting point of the journey
    def get_start_point(self, station, jrny_type):
        self.journey['start'] = station
        self.jrny_type = jrny_type
        return self
    
    #setting the end point of the journey
    def get_end_point(self, station):
        self.journey['end'] = station
        return self
    
    #getting total journey cost
    def get_journey_cost(self):
        start_station  = self.journey['start']
        start_zone  = self._sf.get_station_info(start_station)
        end_station = self.journey['end']
        end_zone = self._sf.get_station_info(end_station)
        cost = self.get_cost_by_zone(start_zone, end_zone)
        return cost
    
    #getting journey cost w.r.t. zones, start point, end point and minimum fare conditions
    def get_cost_by_zone(self,start_zone, end_zone):
        if(self.jrny_type != 'bus'):
            #print(start_zone, end_zone)
            if((len(start_zone)==1)and (len(end_zone)==1)):
                zones_crossed = abs(int(start_zone[0]) - int(end_zone[0])) +1 
                if((zones_crossed==1) and (start_zone[0]==1) and (end_zone[0]==1)):
                    return self._sf.zone_one_fare
                elif((zones_crossed==1) and (start_zone[0]==2) and (end_zone[0]==2)):
                    return self._sf.one_zone_outside_zone1_fare
                elif((zones_crossed==2) and ((start_zone[0]==1) and (end_zone[0]==2)) or ((start_zone[0]==2) and (end_zone[0]==1))):
                    return self._sf.two_zone_with_zone1_fare
                elif((zones_crossed==2) and ((start_zone[0]==2) and (end_zone[0]==3)) or ((start_zone[0]==3) and (end_zone[0]==2))):
                    return self._sf.two_zone_without_zone1_fare
                elif((zones_crossed>=2)):
                    return self._sf.more_than_two_zones
            else:
                min_fare = []
                if(len(start_zone) > 1):
                    for zone in start_zone:
                        list_zone = []
                        list_zone.append(zone)
                        fare = self.get_cost_by_zone(list_zone, end_zone)
                        min_fare.append(fare)
                    return min(min_fare)
                else:
                    for zone in end_zone:
                        list_zone = []
                        list_zone.append(int(zone))
                        fare = self.get_cost_by_zone(start_zone, list_zone)
                        min_fare.append(fare)
                    return min(min_fare)
        else:
            return self._sf.bus_fare



class Card(object):
    #class for card related services
    
    def __init__(self,current_balance):
        self._journey = Journey()
        self._studfare = StationandFare()
        self.current_balace = current_balance
        
    #deducting the actual fare of the journey and adding the previously deducted max fare at the starting point    
    def actual_fare(self,cost):
        self.current_balance = self.current_balance - cost + _studfare.max_fare


class Testclass(object):
    #class for commute transactions
    
    _current_balance = 30
    def __init__(self):
        self._card = Card(self._current_balance)
        self._card.current_balance = self._current_balance
    
    def initiate_journey(self,current_balance):
        self._current_balance = current_balance - self._card._studfare.max_fare
       
    def main(self):
        print("in the test class")

#testing block
if __name__ == "__main__":
    test = Testclass()
    
	##for journey from Holborn to earl's court
    start_station = "Holborn"
    end_station = "Earl's Court"
    jrny_type = 'tube'
    test.initiate_journey(test._current_balance)
    test._card._journey.get_start_point(start_station, jrny_type)
    test._card._journey.get_end_point(end_station)
    journey_cost = test._card._journey.get_journey_cost()
    print("The cost of Journey from {} - {} is {}".format(start_station,end_station,journey_cost))
    print("The current balance in the Oyster Card is {}".format(round(test._current_balance,2)))
    print("\n")
	
    ##for next journey, from Earl's court to chelsea
    start_station = "Earl's Court"
    end_station = "Chelsea"
    jrny_type = 'bus'
    test.initiate_journey(test._current_balance)
    test._card._journey.get_start_point(start_station, jrny_type)
    test._card._journey.get_end_point(end_station)
    journey_cost = test._card._journey.get_journey_cost()
    print("The cost of Journey from {} - {} is {}".format(start_station,end_station,journey_cost))
    print("The current balance in the Oyster Card is {}".format(round(test._current_balance,2)))
    print("\n")
	
    ##for next journey, from Earl's court to Hammersmith
    start_station = "Earl's Court"
    end_station = "Hammersmith"
    jrny_type = 'tube'
    test.initiate_journey(test._current_balance)
    test._card._journey.get_start_point(start_station, jrny_type)
    test._card._journey.get_end_point(end_station)
    journey_cost = test._card._journey.get_journey_cost()
    print("The cost of Journey from {} - {} is {}".format(start_station,end_station,journey_cost))
    print("The current balance in the Oyster Card is {}".format(round(test._current_balance,2)))
    print("\n")
    



