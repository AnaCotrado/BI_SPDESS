import sys
sys.path.append('D:\\UPT\\2021-II\\Inteligencia de Negocios\\Proyecto')

from BD.sql import clsSQL

import tweepy

consumer_key='OEZXAE9fZa5KZ0twwY3QGo2Mm'
consumer_key_secret='G08WPSSZ4S392YgV9lkj5iYyCj3WY0un2p7leFzo4hLQnShIR5'
access_token='889982096172879872-MwgiOpVNFeM2jRbz9SWTnuO2Dd2djOj'
access_token_secret='xX6c3TKMTXbZl7XlNp4kS6t883tIsgTo7Rb6kJ9ORhDQJ'

auth=tweepy.OAuthHandler(consumer_key,consumer_key_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

sql = clsSQL()
id_anterior = "1467745701446795266"

timeline_IGP = api.user_timeline(screen_name = "Sismos_Peru_IGP", since_id = id_anterior, tweet_mode = 'extended')

for tweet in timeline_IGP:
    print(tweet.id)
    id = tweet.id
    url = 'https://twitter.com/igp_peru/status/' + tweet.id_str
    try:
        text = str(tweet.full_text)
    except AttributeError:
        text = str(tweet.text)
    query = ("INSERT INTO TwitterIGP (TweetID, TweetText, TweetUrl) VALUES ({0}, '{1}', '{2}');".format(id, text, url))
    print(query)
    sql.sqlInsert(query)

#3250
#1467745701446795266
#1464911018061144067
#print(len("https://twitter.com/igp_peru/status/1467745788633784324"))