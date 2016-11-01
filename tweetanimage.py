import tweepy
import time
import random
import urllib

#AUTHENTICATION
key = open('keys', 'r') #opens the file with the secret keys

CONSUMER_KEY = key.readline().rstrip() #reads each line and strips the NewLine
CONSUMER_SECRET = key.readline().rstrip()
ACCESS_KEY = key.readline().rstrip()
ACCESS_SECRET = key.readline().rstrip()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#MAIN VARIABLES
lat = 0.000 #Starting latitude and longitude
lon = 0.000
sleeping = 60 #Defines the waiting time between the tweets in seconds
increase = 10 #Defines the coordinates increment
iteration = 0 #Number of iterations counter
zoom = 8 #Zoom Level

#MAIN LOOPS GENERATING THE IMAGE
while True:
    test = "https://maps.googleapis.com/maps/api/staticmap?center="+str(lat)+","+str(lon)+"&zoom="+str(zoom)+"&size=800x800&maptype=satellite"
    urllib.urlretrieve(test, "image"+".png") #Saves the image overwriting the existing one
    time.sleep(15)
    api.update_with_media('image.png',"A random piece of earth. Nr. "+str(iteration)+" Lat: "+str(lat)+" Lon: "+str(lon))
    iteration = iteration +1
    lon = lon + increase
    if lon >= 180:
        lon = -180
        lat = lat + increase
        if lat >= 90:
            lat = -90
    time.sleep(sleeping)
