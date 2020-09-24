#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import csv

# Twitter API credentials
consumer_key = "tXXkW2odMQHc5C9o9jTrFD6X3"
consumer_secret = "Er74zPGo3DFHvWAYgmFETqbyRWNDoQmEKjrXC2pQ4AOiB7ktXF"
access_key = "926208028923240448-Eqz66G4HXDkK1v16d88KVYQJim7sMwr"
access_secret = "C5BHJilABLnv7TaCTJbAvRuJeLdfMKKAvig9RBdjvf9sX"


def get_all_tweets(count,screen_name):
    print("hello {}".format(screen_name))    # Twitter only allows access to a users most recent 3240 tweets with this method
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []
    # make initial request for most recent tweets (200 is the maximum allowed count)
    try:
        new_tweets = api.user_timeline(screen_name=screen_name, count=5, tweet_mode='extended')
        # print(new_tweets)
        # save most recent tweets
        alltweets.extend(new_tweets)
    except tweepy.TweepError:
        print("Failed to run the command on that user, Skipping...")

    # save the id of the oldest tweet less one
    # if(len(alltweets)!=0):
    #     oldest = alltweets[-1].id - 1
    #     print(oldest)
    #     # keep grabbing tweets until there are no tweets left to grab
    #     while len(new_tweets) > 0:
    #         print("getting tweets before %s" % (oldest))
    #
    #         # all subsiquent requests use the max_id param to prevent duplicates
    #         new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
    #         alltweets.extend(new_tweets) # save most recent tweets
    #         oldest = alltweets[-1].id - 1 # update the id of the oldest tweet less one
    #         print("...%s tweets downloaded so far" % (len(alltweets)))
    # else:
    #     print("no tweets detected")
    # transform the tweepy tweets into a 2D array that will populate the csv
    print(type(alltweets[0]))
    outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text.encode("utf-8")] for tweet in alltweets]
    print(len(outtweets))

    # write the csv
    with open('%d %s_tweets.csv'%(count,screen_name), 'w') as f:
    # with open(name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id", "created_at", "text"])
        writer.writerows(outtweets)
    pass
    return len(outtweets)

from DBRepository.UserAllRepository import UserAllRepository as UserAllRepo
from DBRepository.DepressionRepository import DepressionRepository as DPrepo
from Model.User import User
def load_item_from_collection(repo):
    DBTweets = repo.read()
    isSuccess = False
    tweets = []
    for tweet in DBTweets:
        isSuccess = True
        tem_tweet = User.build_from_json(tweet)
        tweets.append(tem_tweet)
    if not isSuccess:
        print("Belum ada di database")
    return tweets
def cetak_username(tweets):
    for tem_tweet in tweets:
        print("ID= {} | username = {} | date = {} | tweet = {} | tweet_id = {} | state = {}".format(tem_tweet._id,
                                                                                                    tem_tweet.username,
                                                                                                    tem_tweet.date,
                                                                                                    tem_tweet.text,
                                                                                                    tem_tweet.tweet_id,
                                                                                                    tem_tweet.state))

# load and return all username from mongodb
def getAllUsernames(tweets):
    usernames = []
    i = 0
    for data in tweets:
        # print(i)
        i = i + 1
        usernames.append(data.username)
    return usernames

# just print out all username
def printUsernames(usernames):
    i = 0
    print(len(usernames))
    for username in usernames:
        print("No: {} | username : {}".format(i,username))
        i = i + 1
    pass


if __name__ == '__main__':
    # doWithPensProxy()
    print("Load Items in 'User All' Collection")
    userAll_repo = UserAllRepo()
    # print(user_repo)
    userAll= load_item_from_collection(userAll_repo)

    usernames=[]
    usernames = getAllUsernames(userAll)
    # printUsernames(usernames)
    userRecord = [[]]

    i=-1;
    for i in range(2):
    # for name in usernames:
            i = i + 1
            if(i<0):
                print("skip")
            else:
                print(i)
                print(usernames[i])
                # print(name)
                jumlahTweetUser = get_all_tweets(i,usernames[i])
                temp = [i,jumlahTweetUser]
                print(temp)
                userRecord.insert(i, temp)
                print(userRecord)

    temp = [1,707],[2,404]
    with open('countTweets.csv', 'w') as f:
        # with open(name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["id_userALL", "jumlah_tweet"])
        writer.writerows(userRecord)
    pass

    # dpRepo = DPrepo()
    # dpTweet = load_item_from_collection(dpRepo)
    # cetak_username(dpTweet)

    # pass in the username of the account you want to download
    name = "realDonaldTrump"
    # get_all_tweets(name)
    pass
