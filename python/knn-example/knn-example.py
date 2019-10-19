#!/usr/local/bin/python3

import operator
import pandas as pd
import numpy as np
from scipy import spatial


r_cols = ['user_id', 'movie_id', 'rating']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols, usecols=range(3))
ratings.head()

movieProperties = ratings.groupby('movie_id').agg({'rating': [np.size, np.mean]})
# movieProperties.head()

movieNumRatings = pd.DataFrame(movieProperties['rating']['size'])
movieNormalizedNumRatings = movieNumRatings.apply(lambda x: (x - np.min(x)) / (np.max(x) - np.min(x)))
# movieNormalizedNumRatings.head()


def ComputeDistance(a, b):
    genresA = a[1]
    genresB = b[1]

    genreDistance = spatial.distance.cosine(genresA, genresB)

    popularityA = a[2]
    popularityB = b[2]

    popularityDistance = abs(popularityA - popularityB)

    return genreDistance + popularityDistance

def getNeighbors(movieID, K):
    
    distances = []
    for movie in movieDict:
        if (movie != movieID):
            dist = ComputeDistance(movieDict[movieID], movieDict[movie])
            distances.append((movie, dist))
    distances.sort(key=operator.itemgetter(1))

    neighbors = []
    for x in range(K):
        neighbors.append((distances[x][0], distances[x][1]))
    return neighbors

movieDict = {}
with open(r'ml-100k/u.item', encoding="ISO-8859-1") as f:
    temp = ''
    for line in f:
        fields = line.rstrip('\n').split('|')
        movieID = int(fields[0])
        name = fields[1]
        genres = fields[5:25]
        genres = map(int, genres)
        movieDict[movieID] = (name, np.array(list(genres)), movieNormalizedNumRatings.loc[movieID].get('size'), movieProperties.loc[movieID].rating.get('mean'))

print(movieDict)
print("Two Movies \n", movieDict[2], movieDict[1016])
print("Compute Distance \n", ComputeDistance(movieDict[2], movieDict[1016]))

K = 10
avgRating = 0
selectedMovieID = 2

print("Selected Movie:", movieDict[selectedMovieID][0], "\n")
print("Similar Movies: \n")

neighbors = getNeighbors(selectedMovieID, K)

for neighbor in neighbors:
    avgRating += movieDict[neighbor[0]][3]
    print (str(neighbor[0]) + " | " + movieDict[neighbor[0]][0] + " | " + str(movieDict[neighbor[0]][3]) + " | " + str(neighbor[1]))
    
# print("Selected Movies Average Rating")
# print(avgRating/K)
