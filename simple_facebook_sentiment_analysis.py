#!/usr/bin/env python

##########################################
#
# simple_facebook_sentiment_analysis.py: Basic script to retrieve and perform Sentiment Analysis on Facebook Posts.
#
# Author: Cosimo Iaia <cosimo.iaia@gmail.com>
# Date: 5/11/2016
#
# This file is distribuited under the terms of GNU General Public
#
#########################################


import facebook as fb
import requests
import argparse
import textblob as tb

FLAGS = None

def sentiment_analysis(post):

    # Here's where the magic happens
    tb_msg = tb(post['message'])
    score = tb_msg.sentiment

    print("Date: %s, From: %s\n", post['created_time'], post['from'])
    print("%s\nShared: %s, Score: %f", post['message'], post['share'], score)



def connect(access_token, user):
    graph = fb.GraphAPI(access_token)
    profile = graph.get_object(user)

    return graph, profile


def main():

    access_token = FLAGS.access_token
    user = FLAGS.profile

    graph, profile = connect(access_token, user)
    
    posts = graph.get_connections(profile['id'], 'posts')


    #Let's grab all the posts and analyze them!
    while True:
        try:
            [sentiment_analysis(post=post) for post in posts['data']]
            posts= requests.get(posts['paging']['next']).json()
        except KeyError:
            break
            


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple Facebook Sentiment Analysis Script')
    parser.add_argument('--access_token', type=str, required=True, default='', help='Your Facebook API Access Token: https://developers.facebook.com/docs/graph-api/overview')
    parser.add_argument('--profile', type=str, required=True, default='', help='The profile name to retrieve the posts from')
    FLAGS = parser.parse_args()
    main()
