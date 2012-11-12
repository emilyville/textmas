#!/usr/bin/python

import argparse
import serial
import simplejson
import sys
import time
import urllib2

def main(argc=None):
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
                f = urllib2.urlopen(
                        ("https://api.twilio.com/2010-04-01/Accounts/%(sid)s/SMS/"+
                         "Messages.json?To=%(tel)s&PageSize=1") % \
                        {'sid': args.account_sid, 'tel': args.incoming_number})
                json_contents = f.read()
                json = simplejson.loads(json_contents)
                message = json["sms_messages"][0]["body"]
                message_low = message.lower()
                if "yellow" in message_low:
                        set_colors(yellow=True)

                if "blue" in message_low:
                        set_colors(blue=True)

                if "red" in message_low:
                        set_colors(red=True)

                if "white" in message_low:
                        set_colors(white=True)

                if "purple" in message_low:
                        set_colors(red=True, blue=True)

                if "green" in message_low:
                        set_colors(yellow=True, blue=True)

                if "orange" in message_low:
                        set_colors(yellow=True, red=True)

                if "rainbow" in message_low:
                        set_colors(True, True, True, True)

                time.sleep(5)


def set_colors(red=False, blue=False, yellow=False, white=False):
        if (red):
                ser.write('a')
        else:
                ser.write('b')

        if (blue):
                ser.write('g')
        else:
                ser.write('h')

        if (white):
                ser.write('c')
        else:
                ser.write('d')

        if (yellow):
                ser.write('e')
        else:
                ser.write('f')

if __name__ == "__main__":
        sys.exit(main())
