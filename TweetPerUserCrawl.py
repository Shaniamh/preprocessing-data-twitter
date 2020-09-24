#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv

# Twitter API credentials
consumer_key = "gXKhvAg1OWhw5MVtQ2KuGXiDQ"
consumer_secret = "kB6CF45ZoE2Y8vzJh9KxdObcTMuoBew4ByP4E8o66tUxQFX2bX"
access_key = "940531793672921088-pXiZcctGoURnvzPjYtMYLJxs89iYgo5"
access_secret = "jofnOAci42fnW13Y5MTeb7Tfsk0ZvTY6TKsz4LiCyVn3k"


def get_all_tweets(screen_name):
    print("hello")
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # print(new_tweets)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    print(oldest)

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print("getting tweets before %s" % (oldest))

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))


    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    print(len(outtweets))
    # for tweet in outtweets:
        # print(tweet)

    # write the csv
    with open('%s_tweets.csv' %screen_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)

    pass


if __name__ == '__main__':
    # pass in the username of the account you want to download
    name = "e100ss"
    get_all_tweets(name)
    # nms = [[1,2]]
    # with open('%s_tweets.csv' %name, 'w') as f:
    #     writer = csv.writer(f)
    #     for row in nms:
    #         # writer.writerow(row)
    #     writer.writerow(["id", "created_at", "text"])
    #     # writer.writerows(outtweets)

    pass
