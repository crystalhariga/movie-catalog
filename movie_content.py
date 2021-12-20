from readData import readData
import pandas as pd
import requests

# Class to return MovieContent

class MovieContent:
    movie = readData.movie()
    link = readData.link()
    rating = readData.rating()
    tag = readData.tag()    
    @staticmethod
    def checkCategory(value):
        # return category based on value
        genres = MovieContent.movie.drop(["movieId", "title"], axis = 1)
        #print(genres)
        title = MovieContent.movie[["movieId", "title"]]
        tagz = MovieContent.tag.drop(["count"], axis = 1)
        if value in genres.values:
            #print("genre")
            return "genre"
        elif title['title'].str.contains(value, case = False).any():
            #print("title")
            return "title"
        else:
            #if tagz['tag'].str.contains(value, case = False).any():
            #print("tag")
            return "tag"

            
    @staticmethod
    def matchRows(datacategory, matchvalue):
        # check with readData to match with matchvalue
        if datacategory == "genre":
            moviess = MovieContent.movie
            data = moviess.loc[moviess.values == matchvalue]
            movieID = data["movieId"].values.tolist()
            #moviess["new"] = (moviess.values == matchvalue).any(1).astype(int)
            #if moviess["new"] == 1: movieID = moviess["movieId"].values.tolist()
            #print(movieID)
            return movieID
        elif datacategory == "title":
            movies = MovieContent.movie
            movie = movies.loc[movies['title'].str.contains(matchvalue, case = False)]
            #print(movie)
            movieID = movie["movieId"].values.tolist()
            #print(movieID)
            return movieID
        elif datacategory == "tag":
            tagg = MovieContent.tag
            movie = tagg.loc[tagg['tag'].str.contains(matchvalue, case = False)]
            #print(movie)
            movieID = movie["movieId"].values.tolist()
            #print(movieID)
            return movieID
        else: return False
    @staticmethod
    def checkRating(movieID):
        # based on movieID list, sort by rating and return 10
        df = MovieContent.rating
        s = []
        for i in movieID:
            s.append(df.loc[df['movieId'] == i])
        data = pd.concat(s)
        data = data.sort_values(by=["rating"], ascending = False)
        top10 = data.iloc[:10]
        top10 = top10["movieId"].values.tolist()
        return top10
            
    @staticmethod
    def get_movie_images(movie_id):
        # get movie images via API from themoviedb
        api_key = 'e9716fa6ef030b65709e3fbeda58c15b'
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language'
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            poster_path = data['poster_path']
            full_path = 'http://placehold.jp/dedede/2e2e2e/150x250.png?text=Image%20Not%20Found' if not poster_path \
                else f'https://image.tmdb.org/t/p/w500/{poster_path}'
            return full_path
        else:
            full_path = "http://placehold.jp/dedede/2e2e2e/150x250.png?text=Image%20Not%20Found"
            return full_path
    
    @classmethod    
    def get_movie_info(self, movieId):
        # movie information based on input values
        movie_info = {}
        # movie title & genres
        moviess = MovieContent.movie.loc[MovieContent.movie['movieId'] == movieId]
        title = moviess['title'].values[0]
        movies = moviess.drop(["movieId", "title"], axis = 1)
        genre = []
        for (columnName, columnData) in movies.iteritems():
            if columnData.values[0] != None:
                genre.append(columnData.values[0])
                continue
            else: break
        #print(title)
        #print(genre)
        
        
        # image
        tmdb = MovieContent.link.loc[MovieContent.link['movieId'] == movieId]
        tmdb = tmdb['tmdbId'].values[0]
        img = MovieContent.get_movie_images(tmdb)
        #print(img)
        
        # rating
        rate = MovieContent.rating.loc[MovieContent.rating['movieId'] == movieId]
        rate = rate['rating'].values[0]
        #print(rate)
        
        # tags & count
        tagzz = MovieContent.tag.loc[MovieContent.tag['movieId'] == movieId]
        tag = tagzz['tag'].to_list()
        #print(len(tag))
        count = tagzz['count'].to_list()
        #print(count)
        
        # append to dictionary!
        # movieId, title, genres, image (full_path), rating, tags, tag counts
        movie_info.update({
            "movieId": movieId,
            "title": title,
            "genres": genre,
            "image": img,
            "rating": rate,
            "tag": tag,
            "tag_ct": count})
        #print(movie_info)
        return movie_info
    

def main():
        movieId = 1
        movielist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        #MovieContent.get_movie_info(movieId)
        #MovieContent.matchRows("tag", "animation") #genre, title, tag
        #MovieContent.checkCategory("mindless")
        #MovieContent.checkRating(movielist)
        #MovieContent.get_movie_images(movieId)
        
        #print(movie.head(n=12))

if __name__ == "__main__":
    main()