#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'zZsZPhSQmKqf7Z4bVLRnBTNxj'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '0f5rdmyvNnyXbTk22JNQyNZkXPfLdGt7RPMedEnj4HfP3dl04j'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '310737527-D3wsjJ46vm0b8hPC0PIqbB0A8BGzYoEiaAHhWEma'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'zPBDJfXWrpdOExvPnnjSKVwH3apZOi2iUsK2Qv84FUAeA'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(status = line)
    time.sleep(20)#Tweet every 20s
