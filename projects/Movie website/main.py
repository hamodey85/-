import media
import fresh_tomatoes
import data

# instance Movies
Dark_Knight = media.Movie(data.Dark_Knight)
Godfather = media.Movie(data.Godfather)
The_Lord_of_the_Rings = media.Movie(data.The_Lord_of_the_Rings)
Shawshank = media.Movie(data.Shawshank)
Forrest_Gump = media.Movie(data.Forrest_Gump)
goodBadUgly = media.Movie(data.goodBadUgly)
toy_story_data = media.Movie(data.toy_story_data)


# putting all instances in array
movies = [Dark_Knight,Godfather,The_Lord_of_the_Rings,Shawshank,Forrest_Gump,goodBadUgly,toy_story_data]

# create the website and open it
fresh_tomatoes.open_movies_page(movies)
