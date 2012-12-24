#!/usr/bin/python

import argparse
import serial
import simplejson
import sys
import time
import urllib2

RED = 1 << 0
BLUE = 1 << 1
YELLOW = 1 << 2
WHITE = 1 << 3

def main():
        parser = argparse.ArgumentParser(
                description='Control Arduino via serial interface')
        parser.add_argument('--account_sid', required=True)
        parser.add_argument('--auth_token', required=True)
        parser.add_argument('--incoming_number', required=True)
        parser.add_argument('--port', default='/dev/ttyACM0')

        args = parser.parse_args()

        ser = serial.Serial(args.port, 9600, timeout=1)

        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        top_level_url = "https://api.twilio.com/"
        password_mgr.add_password(None, top_level_url,
                                  args.account_sid, args.auth_token)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
	current_colors = 0
	last_message = 0
        while(1):
                url = ("https://api.twilio.com/2010-04-01/Accounts/%(sid)s/SMS/"+
                         "Messages.json?To=%(tel)s&PageSize=1") % \
                        {'sid': args.account_sid, 'tel': args.incoming_number}
                try: 
                        f = urllib2.urlopen(url)
                        json_contents = f.read()
                        json = simplejson.loads(json_contents)
			sid = json["sms_messages"][0]["sid"]
			if last_message == sid:
				time.sleep(5)
				continue
			last_message = sid
                        message = json["sms_messages"][0]["body"].lower()
                        colors = 0
                        color_set = False
                        if "yellow" in message:
                                colors |= YELLOW
                                color_set = True

                        if "blue" in message:
                                colors |= BLUE 
                                color_set = True

                        if "red" in message:
                                colors |= RED
                                color_set = True

                        if "white" in message:
                                colors |= WHITE
                                color_set = True

                        if "purple" in message:
                                colors |= RED | BLUE
                                color_set = True

                        if "green" in message:
                                colors |= BLUE | YELLOW
                                color_set = True

                        if "orange" in message:
                                colors |= RED | YELLOW
                                color_set = True

                        if "pink" in message:
                                colors |= RED | WHITE
                                color_set = True

                        if ("rainbow" or "all") in message:
                                colors |= RED | YELLOW | BLUE | WHITE
                                color_set = True

                        if "none" in message:
                                colors = 0
                                color_set = True

			if "cheer" in message:
				set_colors(ser, RED)
				time.sleep(.5)
				set_colors(ser, RED | WHITE)
				time.sleep(.5)
				set_colors(ser, RED | WHITE | YELLOW)
				time.sleep(.5)
				set_colors(ser, RED | WHITE | YELLOW | BLUE)
				time.sleep(.5)
				set_colors(ser, WHITE | BLUE)
				time.sleep(.5)
				set_colors(ser, RED | YELLOW)
				time.sleep(.5)
				set_colors(ser, WHITE | BLUE)
				time.sleep(.5)
				set_colors(ser, RED | YELLOW)

                        if color_set:
				current_colors = colors
			
			if ("blink" or "twinkle" or "flash") in message:
				set_colors(ser, current_colors)
				time.sleep(.25)
				set_colors(ser, 0)
				time.sleep(.25)
				set_colors(ser, current_colors)
				time.sleep(.25)
				set_colors(ser, 0)
				time.sleep(.25)
				set_colors(ser, current_colors)
				time.sleep(.25)
				set_colors(ser, 0)
				time.sleep(.25)
	
			set_colors(ser, current_colors)

                except urllib2.URLError:
                        pass
                time.sleep(5)


def set_colors(ser, colors):
        if (RED & colors > 0):
                ser.write('a')
        else:
                ser.write('b')

        if (BLUE & colors > 0):
                ser.write('g')
        else:
                ser.write('h')

        if (WHITE & colors > 0):
                ser.write('c')
        else:
                ser.write('d')

        if (YELLOW & colors > 0):
                ser.write('e')
        else:
                ser.write('f')

if __name__ == "__main__":
        sys.exit(main())
