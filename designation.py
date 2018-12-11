import psycopg2
import os


def getDesignation(countyCode, tractCode):
    # if type(countyCode) != str or type(tractCode): #if addr is not a string, throws error
    #    raise ValueError('countyCode and tractCode must be type str')
     DATABASE_URL = os.environ['DATABASE_URL']

    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # conn = psycopg2.connect(database="hub_designations", user="django", password="DUHJANGO", host="127.0.0.1", port="5432") #specifies connection details
    cur = conn.cursor() #Creates cursor, which establishes connection

    # Creates dictionary to hold results. This is conviniently the same format as the dictionary in getInHub.py
    info = {    'county':{ 'name':"", 'prevYearDes':False, 'currYearDes':False, 'prevYearReason':"", 'currYearReason':""},
                'tract':{ 'prevYearDes':False, 'currYearDes':False} }

    # Puts single quotes around codes, for correct formatting of SELECT operations below
    countyCode = "'" + countyCode + "'"
    tractCode = "'" + tractCode + "'"

    # Executes SELECT operations on the database for designations and county name
    cur.execute("select county_name FROM county_designations WHERE county_code = " + countyCode)
    info['county']['name'] = cur.fetchall()[0][0]
    cur.execute("select july_2017_status FROM county_designations WHERE county_code = " + countyCode)
    cPrev = cur.fetchall()[0][0]
    cur.execute("select january_2018_status FROM county_designations WHERE county_code = " + countyCode)
    cCurr = cur.fetchall()[0][0]
    cur.execute("select january_2017_status FROM tract_designations WHERE tract_code = " + tractCode)
    tPrev = cur.fetchall()[0][0]
    cur.execute("select january_2018_status FROM tract_designations WHERE tract_code = " + tractCode)
    tCurr = cur.fetchall()[0][0]

    # Decides wether to add reason and decide if qualified. There are three
    # possible states for county designation. "Not Qualified", "Qualified by ...",
    # and "Redesignated until..."

    # This will set reason to the description given by the database if the state
    # is Qualified or Redesignated, but will leave reason blank if state is
    # Not Qualified. It will set the designation to True only if state is Qualified.

    if "Not" not in cPrev:
        info['county']['prevYearReason'] = cPrev
        if 'Qualified' in cPrev:
            info['county']['prevYearDes'] = True
    if "Not" not in cCurr:
        info['county']['currYearReason'] = cCurr
        if 'Qualified' in cCurr:
            info['county']['currYearDes'] = True

    # This sets the designation for tract designations
    if 'Qualified' in tPrev and "Not" not in tPrev:
        info['tract']['prevYearDes'] = True
    if 'Qualified' in tCurr and "Not" not in tCurr:
        info['tract']['currYearDes'] = True


    # This would commit changes made by operations, but since we're only doing
    # select operations, it's unnecesary.
    # conn.commit()

    conn.close() #Closes connection with database

    return info #returns the dictionary
