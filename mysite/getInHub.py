import requests
import simplejson as json
import designation


key = "AIzaSyAjvwJNScsue25L0Zau-fawRYwQekmQFsg"

def getCoord(addr): #takes plaintext address and returns coordinates
    payload = {'address':addr, 'key':key} #puts paramaters for url in dictionary, to be passed in next line
    mapsResponse = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload) #makes request using url
    mapsResponse.raise_for_status() #raises error if request fails
    mapsJson = json.loads(mapsResponse.text) #parses json-formatted response from plaintext into dictionary
    locInfo = { 'lat':mapsJson['results'][0]['geometry']['location']['lat'],
                'lng':mapsJson['results'][0]['geometry']['location']['lng'],
                'faddr':mapsJson['results'][0]['formatted_address']}
    return locInfo #returns a dictionary with two lat and lng and faddr

def getAddr(lat,lng): #takes latitude and longitude and return formatted address
    payload = {'latlng':(str(lat) + ',' + str(lng)), 'key':key} #puts paramaters for url in dictionary, to be passed in next line
    mapsResponse = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload) #makes request using url
    mapsResponse.raise_for_status() #raises error if request fails
    mapsJson = json.loads(mapsResponse.text)#parses json-formatted response from plaintext into dictionary
    return mapsJson['results'][1]['formatted_address'] #returns formatted address as string

def getCT(lat,lng): #takes latitude and longitude and returns census tract number
    payload = {'x':lng, 'y':lat, 'benchmark':"Public_AR_Census2010", 'vintage':'Census2010_Census2010', 'layers':'14', 'format':'json'} #puts paramaters for url in dictionary, to be passed in next line
    censusResponse = requests.get('https://geocoding.geo.census.gov/geocoder/geographies/coordinates', params=payload) #makes request using url
    censusResponse.raise_for_status() #raises error if request fails
    censusJson = json.loads(censusResponse.text) #parses json-formatted response from plaintext into dictionary
    #11-digit census tract numbers are formatted 'XXYYYZZZZZZ' XX are state code,
    #YYY are county code and ZZZZZZ are tract code
    state = str(censusJson['result']['geographies']['Census Blocks'][0]['STATE']) #Pulls each code from json dictionary
    county = str(censusJson['result']['geographies']['Census Blocks'][0]['COUNTY'])
    tract = str(censusJson['result']['geographies']['Census Blocks'][0]['TRACT'])
    tractFull = state + county + tract #conbines codes into an 11-digit code
    countyFull = state + county #combines codes into a 5-digit county code
    return {'tract':tractFull, 'county':countyFull} #returns dictionary containing tract and county codes


class location():
    locSet = False #bool for wether the location has been set
    addressString = "" #inputted the string for the address. May be left blank if location is set from coordinates
    faddress = "" #formatted address from maps api call
    lat = "0" #string representations of coordinates
    lng = "0"
    tractCode = "0" #tract and county codes
    countyCode = "0"
    designated = False
    designationInfo = {    'county':{ 'name':"", 'prevYearDes':False, 'currYearDes':False, 'prevYearReason':"", 'currYearReason':""},
                'tract':{ 'prevYearDes':False, 'currYearDes':False} }

    def __init__(self,addr): #constructor. Takes addr string as input. If addr == "", constructor will not set location, but will construct class
        if type(addr) != str: #if addr is not a string, throws error
            raise ValueError('addr must be type str')
        if addr != "": #only sets location if addr isn't blank
            locInfo = getCoord(addr) #Gets coordinates from google maps api, using plaintext address as input
            self.lat = str(locInfo['lat']) #sets lat, lng, and faddress values and sets locSet to true
            self.lng = str(locInfo['lng'])
            self.faddress = locInfo['faddr']
            self.locSet = True
            codes = getCT(self.lat,self.lng) #pulls tract and county codes from census api
            self.tractCode = codes['tract']
            self.countyCode = codes['county']

            self.designationInfo = designation.getDesignation(self.countyCode,self.tractCode) #pulls designation from database
            self.designated = self.designationInfo['county']['currYearDes'] or self.designationInfo['tract']['currYearDes'] #sets overall designation to true or false


    # if addr in constructor was left blank, this can be used to set the
    #location using coordinates. It can take input str or float as input
    def setByLL(self,lat,lng):
        # if input is not of correct form, raise error
        if (type(lat) == float or type(lat) == str) and (type(lng) == float or type(lng) == str):
            raise ValueError('setByLL(lat,lng) requires lat and lng to both be of type float or str')
        #else
        self.lat = str(lat) #sets lat and lng values and sets locSet to true
        self.lng = str(lng)
        self.addr = getAddr(lat,lng) #pulls address from google api
        self.faddr = self.addr
        self.locSet = True
        codes = getCT(lat,lng) #pulls tract and county codes from census api
        self.tractCode = codes['tract']
        self.countyCode = codes['county']


"""
userIn = input("Enter Address: \t") #takes input of address
userLoc = location(userIn) #creates location class using address, which also pulls coordinates from google maps api, and tract and county codes from census api
print(userLoc.tractCode) #prints tract code
print(userLoc.countyCode) #prints county code
"""
