# Movie Recommender App 2021
*Update (2022/02/03): Search filtering does not work as expected*
Issues:
- can't seem to match genres and tags, since the search query only looks for movie titles


### Summary
- Designed a data dictionary from 4 datasets for ease of accessibility to display movie information onto Movie Catalog web app
- Designed a search algorithm (filtering), by checking whether the search query matches the movie information available (*still needs improvement*)
- Designed the front-end of web app using Dash, incorporating interactive buttons to search through database
- Implemented movie images using API from [themoviedb](https://www.themoviedb.org/)


### Background
- End-to-end data analytics project using datasets from [MovieLens](https://grouplens.org/datasets/movielens/25m/) containing 25M movie ratings


### Description of Files
- [movie_content.py](https://github.com/crystalhariga/movie-recommender-2021/blob/main/movie_content.py): Class file to **return movie information** and **check search value with movie information**
- [movie_recommender.py](https://github.com/crystalhariga/movie-recommender-2021/blob/main/movie_recommender.py): Main file to **run the movie recommender web app**
- [readData.py](https://github.com/crystalhariga/movie-recommender-2021/blob/main/readData.py): Class file to **read and clean** the movie dataset
- [topBar.py](https://github.com/crystalhariga/movie-recommender-2021/blob/main/topBar.py): Class file to **return navigation bar** for the web app

### Demo

https://user-images.githubusercontent.com/34080006/152404390-bca524f3-21eb-4ef1-8386-fe9135503b52.mov

