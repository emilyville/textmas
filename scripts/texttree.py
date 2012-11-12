#!/usr/bin/python

import serial
import simplejson
import time
import urllib2


ser = serial.Serial('/dev/tty.usbmodemfa141', 9600, timeout=1)

while(1):
	password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
	top_level_url = "https://api.twilio.com/"
	password_mgr.add_password(None, top_level_url,
	  'ACa5e089206986232cb31577d95931a62b', 'c03cfdeaa034bf5d9c56758f557e9c1c')
	handler = urllib2.HTTPBasicAuthHandler(password_mgr)
	opener = urllib2.build_opener(handler)
	urllib2.install_opener(opener)
	f = urllib2.urlopen('https://api.twilio.com/2010-04-01/Accounts/ACa5e089206986232cb31577d95931a62b/SMS/Messages.json?To=%2B14153229922&PageSize=1')
	json_contents = f.read()
	print json_contents
	json = simplejson.loads(json_contents)
	message = json["sms_messages"][0]["body"]
	print message

	if message.lower() == "on":
	  ser.write('a')
	elif message.lower() == "off":
	  ser.write('b')
	time.sleep(5)
