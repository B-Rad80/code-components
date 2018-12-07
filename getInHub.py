import requests
import simplejson as json
import designation


key = "AIzaSyAjvwJNScsue25L0Zau-fawRYwQekmQFsg"

def getCoord(addr): #takes plaintext address and returns coordinates
    payload = {'address':addr, 'key':key} #puts paramaters for url in dictionary, to be passed in next line
    mapsResponse = requests.get('https://maps.googleapis.com/maps/api/geocode/json', params=payload) #makes request using url
    mapsJson = json.loads(mapsResponse.text) #parses json-formatted response from plaintext into dictionary

    if int(mapsResponse.status_code) >= 400:
        return {'error':True,
                'errorFatal':True,
                'errorText':'HTTP Error: ' + censusResponse.status_code}
    if mapsJson['status'] != 'OK':
        return {'error':True,
                'errorFatal':True,
                'errorText':mapsJson['status']}

    country = ""
    for item in mapsJson['results'][0]['address_components']:
        if 'country' in item['types']:
            country = item['short_name']
    #print(mapsResponse.text)
    if country == "US":
        locInfo = { 'error':False,
                    'errorText':"",
                    'lat':mapsJson['results'][0]['geometry']['location']['lat'],
                    'lng':mapsJson['results'][0]['geometry']['location']['lng'],
                    'faddr':mapsJson['results'][0]['formatted_address'],
                    'country':country}
    else:
        locInfo = { 'error':True,
                    'errorFatal':False,
                    'errorText':"Not a US Address",
                    'lat':mapsJson['results'][0]['geometry']['location']['lat'],
                    'lng':mapsJson['results'][0]['geometry']['location']['lng'],
                    'faddr':mapsJson['results'][0]['formatted_address'],
                    'country':country}
    return locInfo #returns a dictionary with two lat and lng and faddr

def getCT(lat,lng): #takes latitude and longitude and returns census tract number
    payload = {'x':lng, 'y':lat, 'benchmark':"Public_AR_Census2010", 'vintage':'Census2010_Census2010', 'layers':'14', 'format':'json'} #puts paramaters for url in dictionary, to be passed in next line
    censusResponse = requests.get('https://geocoding.geo.census.gov/geocoder/geographies/coordinates', params=payload) #makes request using url

    if int(censusResponse.status_code) >= 400:
        return {'error':True,
                'errorText':'HTTP Error: ' + censusResponse.status_code}

    censusJson = json.loads(censusResponse.text) #parses json-formatted response from plaintext into dictionary
    #11-digit census tract numbers are formatted 'XXYYYZZZZZZ' XX are state code,
    #YYY are county code and ZZZZZZ are tract code
    state = str(censusJson['result']['geographies']['Census Blocks'][0]['STATE']) #Pulls each code from json dictionary
    county = str(censusJson['result']['geographies']['Census Blocks'][0]['COUNTY'])
    tract = str(censusJson['result']['geographies']['Census Blocks'][0]['TRACT'])
    tractFull = state + county + tract #conbines codes into an 11-digit code
    countyFull = state + county #combines codes into a 5-digit county code
    return {'error':False,
            'errorText':"",
            'tract':tractFull,
            'county':countyFull} #returns dictionary containing tract and county codes


class location():
    locSet = False #bool for wether the location has been set
    addressString = "" #inputted the string for the address. May be left blank if location is set from coordinates
    faddress = "" #formatted address from maps api call
    lat = "0" #string representations of coordinates
    lng = "0"
    tractCode = "0" #tract and county codes
    countyCode = "0"
    designated = False
    applicantName = "" # The name of the person associated with the address
    designationInfo = {    'county':{ 'name':"", 'prevYearDes':False, 'currYearDes':False, 'prevYearReason':"", 'currYearReason':""},
                'tract':{ 'prevYearDes':False, 'currYearDes':False} }

    error = False
    errorText = ""

    def __init__(self,addr): #constructor. Takes addr string as input. If addr == "", constructor will not set location, but will construct class
        if type(addr) != str: #if addr is not a string, throws error
            raise ValueError('addr must be type str')
        if addr != "": #only sets location if addr isn't blank
            locInfo = getCoord(addr) #Gets coordinates from google maps api, using plaintext address as input
            if locInfo['error']:
                self.error = True
                self.errorText = "Maps API ERROR: ' " + locInfo['errorText'] + " '"
                if not locInfo['errorFatal']:
                    self.faddress = locInfo['faddr']
            else:
                self.lat = str(locInfo['lat']) #sets lat, lng, and faddress values and sets locSet to true
                self.lng = str(locInfo['lng'])
                self.faddress = locInfo['faddr']
                self.locSet = True
            if not self.error:
                codes = getCT(self.lat,self.lng) #pulls tract and county codes from census api
                if codes['error']:
                    self.error = True
                    self.errorText = "Census API Error: ' " + codes['errorText'] +" '"
                else:
                    self.tractCode = codes['tract']
                    self.countyCode = codes['county']
            if not self.error:
                self.designationInfo = designation.getDesignation(self.countyCode,self.tractCode) #pulls designation from database
                self.designated = self.designationInfo['county']['currYearDes'] or self.designationInfo['tract']['currYearDes'] #sets overall designation to true or false

    def setName(self, name):
        if type(name) != str:
            raise ValueError('name must be type str')
        self.applicantName = name
