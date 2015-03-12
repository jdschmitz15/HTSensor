#!/usr/bin/python
'''  ********************************************************

Created by: Jeff Schmitz
Date: 3-12-2015

Purpose:
	Built a small script that gathers the temperature and humidity
and makes a call to a restful API.  Passes the device id(which I make up),
temp and humidity.  The date should also have the index and date added.

'''
import Adafruit_DHT

import logging
import logging.config

import requests, json

BASE_HTAPI_URL = "http://192.168.1.221:8000/htdata/"
HEADER = {'content-type': 'application/json'}
DEVICEID = 1
PIN=12
SENSOR=Adafruit_DHT.DHT22
LOGFILE = "logfile"



if __name__ == "__main__":
    logging.basicConfig(filename=LOGFILE)
    logger = logging.getLogger("HTSensor")
    logging.config.fileConfig("log_config")


    #call the DHT22 device hanging off the PIN configured
    try:
        humidity, temp = Adafruit_DHT.read_retry(SENSOR, PIN)
        logger.info("Accessing DHT22 temp = %d and humidity = %d", temp, humidity)
    except IOError as e:
        logging.info("ouch")
    jsondata = json.dumps({'deviceid':DEVICEID,'temp':temp, 'humidity':humidity})
    r = requests.post(BASE_HTAPI_URL, data=jsondata, headers=HEADER)







