# Author: Kristen Findley
# Date: January 24, 2017
# Python: Version 3.5.2
# Description: Notes for SQL with Python tutorial (https://www.youtube.com/watch?v=lhU2OZCKXhQ&feature=youtu.be)

# You can use pythonanywhere.com to interface with mySQL via Python in the cloud

''' USING THE BASH CONSOLE in pythonanywhere.com (u: kfinstotheleft p: (highschoolmascot+soccer#)):

first create new database (named tutorial in this example) and then navigate to BASH under consoles

23:03 ~ $ mysql -ukfinstotheleft -hkfinstotheleft.mysql.server.pythonanywhere-services.com -p (-u is for username, -h stands for host -p for password (bash should then prompt for password))

mysql> SHOW DATABASES; (shows existing databases)
mysql> SHOW PROCESSLIST; (use to see what processes are running and possibly taking up all you CPU!)

mysql> USE kfinstotheleft$tutorial (use to change to the tutorial db)
mysql> CREATE TABLE taula (time int(13),username varchar(20),tweet varchar(40));
mysql> SHOW TABLES;
mysql> DESCRIBE taula;
mysql> INSERT INTO taula VALUES (1385419969,"sentdex","welcome to my tutorial");
mysql> INSERT INTO taula VALUES (1385419970,"sentdex","wow thanks @Obama, you are right these tutorials rock");
mysql> INSERT INTO taula VALUES (1385419971,"sentdex","@BillGates, thanks Bill for the job offer as VP, but I want to keep my options open");
mysql> SELECT * FROM taula

mysql> UPDATE taula SET username = "Sentdex" WHERE username = "sentdex";
mysql> UPDATE taula SET username = "sentdex" WHERE username = "Sentdex" LIMIT 1; (only changes first Sentdex it encounters)
mysql> DELETE FROM taula WHERE username = "sentdex" LIMIT 1; (deletes only one of the sentdex entries, and if called again, will delete even the capitalized Sentdex because varchars are case insensitive)
mysql> SELECT * FROM taula WHERE username = 'sentdex'; (shows all three even despite the case discrepancies... therefore use select as tool to view what will be deleted before deleting)
mysql> SELECT * FROM taula WHERE time > 1385419969 AND time < 1385419971;

###############################################################################################################

USING PYTHON CONSOLE in pythonanywhere.com (see above for username and password)

import MySQLdb
import time

conn = MySQLdb.connect("kfinstotheleft.mysql.pythonanywhere-services.com","kfinstotheleft","jimihendrix","kfinstotheleft$tutorial")
c = conn.cursor()

username = 'Python'
tweet = 'suh-weeeeett dude'
c.execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)", (time.time(), username, tweet))
conn.commit() # saves to db

c.execute("SELECT * FROM taula")
rows = c.fetchall()
for eachRow in rows:
    print(eachRow)

###############################################################################################################

USING TWITTER APIv1.1 WITH PYTHON TO STREAM TWEETS

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'RFw9BXzoSgR6qoN5FZFDy2GlV'
csecret = 'xYSIU6TN1XDDh6nYeX4TIakSVHbfbBhYggdS54IWQYAX1MZrQ5'
atoken = '905110987-MX8aJlz8LWW4S0MqsWzzeJjXLsV8ZrLEJAtoW9Qb'
asecret = 'QiLPLotM6Tz3pUB18Nbm05CUrl0Xu2VXccoGcUeuISHjH'

class listener(StreamListener):
    def on_data(self,data):
         print(data)
         return True

    def on_error(self,status):
         print(status)

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth,listener())
twitterStream.filter(track=["car"])

