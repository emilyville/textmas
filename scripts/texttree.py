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
        while(1):
                url = ("https://api.twilio.com/2010-04-01/Accounts/%(sid)s/SMS/"+
                         "Messages.json?To=%(tel)s&PageSize=1") % \
                        {'sid': args.account_sid, 'tel': args.incoming_number}
                try: 
                        f = urllib2.urlopen(url)
                        json_contents = f.read()
                        json = simplejson.loads(json_contents)
                        message = json["sms_messages"][0]["body"]
                        message_low = message.lower()
                        colors = 0
                        if "yellow" in message_low:
                                colors |= YELLOW

                        if "blue" in message_low:
                                colors |= BLUE 

                        if "red" in message_low:
                                colors |= RED

                        if "white" in message_low:
                                colors |= WHITE

                        if "purple" in message_low:
                                colors |= RED | BLUE

                        if "green" in message_low:
                                colors |= BLUE | YELLOW

                        if "orange" in message_low:
                                colors |= RED | YELLOW

                        if "rainbow" in message_low:
                                colors |= RED | YELLOW | BLUE | WHITE

                        if "none" in message_low:
                                colors = 0
                        set_colors(ser, colors)
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
