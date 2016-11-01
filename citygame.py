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
key.close()

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#MAIN VARIABLES
lat = 0 #Starting latitude and longitude
lon = 0
sleeping = 60 #Defines the waiting time between the tweets in seconds
increase = 0.10 #Defines the coordinates increment
iteration = 0 #Number of iterations counter
zoom = 15 #Zoom Level
random.seed()

#OPENING THE CITIES DATABASE
with open('cities.txt') as f:
    numcities =  sum(1 for _ in f)
    print numcities
    f.close()
    
cities = open('cities.txt','r') #thanks to gael varoquaux for this file
cities = cities.readlines()

#MAIN LOOPS GENERATING THE IMAGE
while True:
    n = random.randrange(1,numcities,1)
    print cities [n]
    cityline = cities[n]
    cityline = cityline.rstrip()
    cityline = cityline.split('\t')
    print cityline
    lon = cityline[1]
    lat = cityline[2]
    test = "https://maps.googleapis.com/maps/api/staticmap?center="+str(lat)+","+str(lon)+"&zoom="+str(zoom)+"&size=640x640&maptype=satellite"
    urllib.urlretrieve(test, "image"+".png") #Saves the image overwriting the existing one
    time.sleep(5) #gives time to fetch the content and save it
    api.update_with_media('image.png',"A random piece of earth. "+cityline[0]+" Lat: "+str(lat)+" Lon: "+str(lon))
    iteration = iteration +1
    time.sleep(sleeping)
