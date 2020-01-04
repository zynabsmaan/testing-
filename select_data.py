import pandas as pd


# Read small data to get the ids of movies
small_medium_movies = pd.read_csv("small_medium_movies.csv", usecols=['movieId'])
ids = small_medium_movies['movieId'].to_numpy().astype('str')
user_movies_interactions_iterator = pd.read_csv("user_movie_interactions.csv", chunksize=5000, usecols=ids
                                                ,header=0)

i = 0
for chunck in user_movies_interactions_iterator :
    print("Chunck {}".format(i))
    # Save dataset user_movies_interactions_reduced
    chunck.to_csv("user_movie_interactions_ch_{}.csv".format(i))
    i += 1




