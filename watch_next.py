import spacy

# creates nlp model
nlp = spacy.load('en_core_web_md')


# function that takes description of movie and returns movie title most similar to it
def similar_movie(description):
    # opens movies.txt file
    with open("movies.txt") as f:
        # creates dictionary which stores the title and similarity score of each movie
        movie_dict = {}

        # iterates through each movie, then generates and adds title and similarity score to movie_dict
        for movie in f.read().split("\n"):
            title = movie.split(":")[0].strip()
            desc = movie.split(":")[1].strip()  # gets description of current movie
            score = nlp(description).similarity(nlp(desc))

            movie_dict[title] = score

        # gets key in movie_dict with highest similarity score
        most_similar = max(movie_dict, key=movie_dict.get)

        return most_similar


# description of hulk movie
hulk_desc = '''Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.'''

# finds and displays title of most similar movie
title = similar_movie(hulk_desc)
print(title)
