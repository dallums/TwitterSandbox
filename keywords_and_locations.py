# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 10:54:18 2017

@author: Abdiel Capital
"""



import tweepy
from tweepy import OAuthHandler
import sys
import operator

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
Owner = 'OWNER'
Owner_ID = 'OWNER_ID'
access_token = 'ACCESS_TOKEN'
access_secret = 'ACCESS_SECRET'
Moscow = [55.7558, 37.6173] #switch lat and long
SanFrancisco = [-122.75,36.8, -121.75,37.8]
NYC = [-73.935242,40.730610]
box_size = 20
keywords = ['Russia']


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
city = NYC
location = [city[0]-box_size, city[1]-box_size, city[0]+box_size, city[1]+box_size]


api = tweepy.API(auth)

#print('Enter search term: ')
#user_name = str(input().strip())
#
#print('\nHere are the search results:')
#for user in api.search_users(user_name):
#    print(user.screen_name)
#    
#user = api.get_user(input())
#
#print(user.description)

class CustomStreamListener(tweepy.StreamListener):  
    global location_dict
    location_dict = {}
    
    def on_status(self, status):
        try:
            city = status.place.full_name
            print city
            #print status.place.bounding_box.coordinates
            try:
                location_dict[city] += 1
            except:
                location_dict[city] = 1
        except:
            try:
                print status.place.country
            except:
                pass
            else:
                pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream



if __name__ == "__main__":
    sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
    sapi.filter(track=keywords)
    #sapi.filter(locations=location)
    sorted_location_dict = sorted(location_dict.items(), key = operator.itemgertter(1), reverse = True)
    
