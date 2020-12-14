"""
The purpose of this module is to utilize the tweepy API to retreive tweets containing
our query term. In this case, we used the API's querying ability to retreive all
tweets from the last month with the "cashtags" $TSLA, $PLTR, and $NFLX. The module was
used to create the respective files tweet_data_tsla.txt, tweet_data_pltr.txt, and
tweet_data_nflx.txt which can be parsed to get the date and time of the tweet as
well as its contents (in string form).
"""

import tweepy
import KeysAndTokens
import datetime
import requests
from requests_oauthlib import OAuth1


# https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets
standard_url = "https://api.twitter.com/1.1/search/tweets.json" # used for testing
# dif args
thirty_day_url = "https://api.twitter.com/1.1/tweets/search/30day/test.json"
full_archive_url = "https://api.twitter.com/1.1/tweets/search/fullarchive/dev.json"



################################################ Premium
end_date = datetime.datetime(2020, 12, 12)
beginning_date_f = datetime.datetime(2020, 11, 30)
beginning_date_t = datetime.datetime(2020, 12, 1)


while beginning_date_f < end_date:

    f_beginning_date = int(str(beginning_date_f.year) + beginning_date_f.strftime('%m') + beginning_date_f.strftime('%d') + '0000')
    t_beginning_date = int(str(beginning_date_t.year) + beginning_date_t.strftime('%m') + beginning_date_t.strftime('%d') + '0000')

    search_params = {
            'query': 'NFLX',
            'fromDate':f_beginning_date,
            'toDate':t_beginning_date,
            'maxResults':10
            } # $cashtag doesn't quite work for querying filter

    response = requests.get(thirty_day_url,
            auth=OAuth1(KeysAndTokens.API_KEY, KeysAndTokens.API_KEY_SECRET, KeysAndTokens.ACCESS_TOKEN, KeysAndTokens.ACCESS_TOKEN_SECRET),
            params=search_params)

    if "error" in response.json().keys():
        print(response.json()['error'])
        exit()

    tweets = response.json()['results']
    file = open("tweet_data_nflx.txt", "a")

    for tweet in tweets:
        file.write("--start--\n")
        file.write(tweet['created_at'] + " : " + "\n")
        file.write(tweet['text'] + "\n" + "--end--")
        file.write("\n")
        file.write("\n")
    file.close()

    PAGES = 9
    page = 0

    while page < PAGES:
        search_params = {
                            'query': 'NFLX',
                            'fromDate':f_beginning_date,
                            'toDate':t_beginning_date,
                            'maxResults':10,
                            'next':response.json()['next']
                            } # $cashtag doesn't quite work for querying filter

        response = requests.get(thirty_day_url,
                            auth=OAuth1(KeysAndTokens.API_KEY, KeysAndTokens.API_KEY_SECRET, KeysAndTokens.ACCESS_TOKEN, KeysAndTokens.ACCESS_TOKEN_SECRET),
                            params=search_params)

        if "error" in response.json().keys(): ######################
            print(response.json()['error'])
            exit()

        tweets = response.json()['results']
        file = open("tweet_data_nflx.txt", "a")

        for tweet in tweets:
            file.write("--start--\n")
            file.write(tweet['created_at'] + " : " + "\n")
            file.write(tweet['text'] + "\n" + "--end--")
            file.write("\n")
            file.write("\n")
        file.close()

        page += 1

    beginning_date_f += datetime.timedelta(days=1)
    beginning_date_t += datetime.timedelta(days=1)

exit()
################################################



"""
################################################ Standard
file_test = open("tweet_data_nflx.txt", "a")

present_date = datetime.datetime(2020, 12, 13)
beginning_date = datetime.datetime(2020, 12, 12)

while beginning_date < present_date:

    relevent_date = str(beginning_date).split()[0] # get rid of hh:mm:ss
    print(relevent_date)

    query_params = {'q': 'NFLX',
                    'lang':'en',
                    'result_type':'recent', #popular, recent, mixed
                    'until':str(relevent_date),
                    'count':100} # $cashtag doesn't quite work for querying filter


    response = requests.get(standard_url,
                        auth=OAuth1(KeysAndTokens.API_KEY, KeysAndTokens.API_KEY_SECRET, KeysAndTokens.ACCESS_TOKEN, KeysAndTokens.ACCESS_TOKEN_SECRET),
                        params=query_params)

    statuses = response.json()['statuses']

    for status in statuses:
        file_test.write("--start--\n")
        file_test.write(status["created_at"] + " : " + "\n")
        file_test.write(status['text'] + "\n" + "--end--")
        file_test.write("\n")
        file_test.write("\n")

    beginning_date += datetime.timedelta(days=1)
file_test.close()

################################################
"""
