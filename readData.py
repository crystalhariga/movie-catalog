# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:14:30 2021

@author: Crystal
"""

import pandas as pd


# Class to read the data and clean

class readData:
    #gscores = pd.read_csv("data/genome-scores.csv")
    #gtags = pd.read_csv("data/genome-tags.csv")
    @classmethod
    def rating(self):
        # Ratings
        ratings = pd.read_csv("data/ratings.csv")
        rating = ratings.groupby('movieId', as_index = False).mean().round(1)
        rating = rating.drop(['userId', 'timestamp'], axis = 1)
        # movieId, rating
        #print(rating.head(n=5))
        return rating
        
    @classmethod
    def link(self):
        # Includes references to other sites
        link = pd.read_csv("data/links.csv")
        link['tmdbId'] = link['tmdbId'].fillna(0.0).astype(int)
        # movieId, imdbId, tmdbId
        #print(link.head(n=5))
        return link
    
    @classmethod
    def movie(self):
        # Includes titles & genres -- use as main data
        movie = pd.read_csv("data/movies.csv")
        movie[['g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9']] = movie['genres'].str.split('|', expand=True)
        movie = movie.drop(['genres'], axis = 1)
        # movieId, title, g0-g9
        #print(movie.head(n=20))
        return movie
    
    @classmethod
    def tag(self):
        # Tags (by user ID -- let's remove user id here to make it a general movie recommender system)
        tags = pd.read_csv("data/tags.csv")
        tags = tags.drop(['userId', 'timestamp'], axis = 1)
        tags = tags.sort_values(by=['movieId'])
        tagss = tags.groupby(['movieId', 'tag']).size().reset_index(name = 'count')
        tagss = tagss.sort_values(by=['movieId', 'count'], ascending = (True, False))
        # movieId, tag, count
        #print(tagss.head(n=10))
        return tagss
     

def main():
        # movie_full = readData.prepData()
        # print(movie_full.head(n = 12))
        movie = readData.movie()
        rating = readData.rating()
        tags = readData.tag()
        link = readData.link()
        #print(movie.head(n=12))

if __name__ == "__main__":
    main()