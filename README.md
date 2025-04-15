#movie-recommendation system
This project implements a content-based movie recommendation system using the TMDB 5000 Movies dataset.
The system suggests similar movies based on features like genres, keywords, cast, crew, and overview.
Features:
Content-based filtering using movie metadata
Text processing with stemming and vectorization
Cosine similarity for finding similar movies
Top 5 recommendations for any given movie

Dataset:
The system uses two datasets from TMDB:
tmdb_5000_movies.csv
tmdb_5000_credits.csv

Data Processing Pipeline:
Merge datasets on movie title
Extract key features: genres, keywords, cast, crew, overview
Convert JSON-formatted columns to lists
Process text data (lowercase, remove spaces, stemming)
Combine all features into tags
Vectorize tags using CountVectorizer

Recommendation Algorithm:
Compute cosine similarity between all movies
For a given movie, find 5 most similar movies based on cosine similarity scores
