#!/usr/bin/python


from weibo import APIClient
import sys, os, urllib, urllib2  
from datetime import date
import time

#from http_helper import *  
#from retry import *  
try: 
    import json  
except ImportError:
    import simplejson as json  


def apply_token(client):
    access_token = '2.00C2FGgDbv7UHB2e35719890tfMLwC'
    expires_in = 1524683076
    try:
        client.set_access_token(access_token, expires_in)
    except StandardError, e:
        if hasattr(e, 'error'):
            if e.error == 'expired_token':
                print "Token is expired"
        else:
            print e
def post_weibo(client, message):
    try:
        #print message

        r = client.statuses.upload.post(status=message, pic=open('/home/pi/Pictures/Home.jpg'))
        #r = client.statuses.update.post(status=message)
    except StandardError, e:
        if hasattr(e, 'error'):
            print e.error

def main():
    client = APIClient(app_key='1026820539', app_secret='9815a7c13eb99018346d0e8f34d6a51e', redirect_uri='http://raspberry.sinaapp.com/callback') 
    apply_token(client)
    post_weibo(client, u'Post a weibo from raspberry pi at %s' % time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time())))


if __name__ == "__main__":
    main()
