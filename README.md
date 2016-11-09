# tweetOmap

A simple bot written in Python using the __Tweepy__ library, it tweets a static image from Google Maps. Resolution can be defined but it's set by default at 640x640 px, it starts from a defined point (lat, lon) and proceeds incrementing the longitude value by a defined value, once it reaches 180°(E) it goes back to -180° (W) and increases also latitude. Once latitude also reaches 90° (N) it goes back to -90° (S) and moves towards the equator. The loop is infinite.

Picture zoom and increment can also be modified.

Please notice that the keys in the "keys" must be in the given order.

###TODO
Define zoom with physical values, km, m, miles, etc.