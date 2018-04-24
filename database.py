import fresh_tomatoes
import main

"""
database.py acts as a database for the project as ut contains all the
information about various instances of the class 'Movie'. This file has all
the information about every single movie that is displayed. This python file
then calls the fresh_tomatoes.py file at the end to open the page in a web
browser.
"""

"""
Movies are defined as:
    movie.title - The title of the movie.
    movie.year - The year the movie got released.
    movie.rating - The rating provided by International Movie Database(IMDb).
    movie.poster_image_url - IMDb Image URL of the movie posters.
    movie.youtube_trailer_url - YouTube trailer URLs of the respective movies.
"""

bird = main.Movie("Birdman",
                  "2014",
                  "IMDb 7.7",
                  "https://goo.gl/oaeUew",
                  "https://www.youtube.com/watch?v=uJfLoE6hanc")

fig = main.Movie("Fight Club",
                 "1999",
                 "IMDb 8.8",
                 "https://goo.gl/1eC2oh",
                 "https://www.youtube.com/watch?v=SUXWAEX2jlg")

forr = main.Movie("Forrest Gump",
                  "1994",
                  "IMDb 8.8",
                  "https://goo.gl/pwJHy4",
                  "https://www.youtube.com/watch?v=rU8repv7uHw")

god = main.Movie("Godzilla",
                 "2014",
                 "IMDb 6.4",
                 "https://goo.gl/Nn3TvC",
                 "https://www.youtube.com/watch?v=I-EEqJ9HyTk")

good = main.Movie("Goodfellas",
                  "1990",
                  "IMDb 8.7",
                  "https://goo.gl/xm7uwv",
                  "https://www.youtube.com/watch?v=2ilzidi_J8Q")

gua = main.Movie("Guardians of the Galaxy",
                 "2014",
                 "IMDb 8.1",
                 "https://goo.gl/fvgGSc",
                 "https://www.youtube.com/watch?v=crIaEzXgqto")

inc = main.Movie("Inception",
                 "2010",
                 "IMDb 8.7",
                 "https://goo.gl/cSDAkx",
                 "https://www.youtube.com/watch?v=8hP9D6kZseM")

pulp = main.Movie("Pulp Fiction",
                  "1994",
                  "IMDb 8.9",
                  "https://goo.gl/xK54K2",
                  "https://www.youtube.com/watch?v=ewlwcEBTvcg")

sch = main.Movie("Schindler's List",
                 "1993",
                 "IMDb 8.9",
                 "https://goo.gl/KqP6dn",
                 "https://www.youtube.com/watch?v=gG22XNhtnoY")

shaw = main.Movie("The Shawshank Redemption",
                  "1994",
                  "IMDb 9.2",
                  "https://goo.gl/Dm5BEy",
                  "https://www.youtube.com/watch?v=6hB3S9bIaco")

godf = main.Movie("The Godfather",
                  "1972",
                  "IMDb 9.2",
                  "https://goo.gl/xgp4x5",
                  "https://www.youtube.com/watch?v=sY1S34973zA")

tom = main.Movie("Tomorrowland",
                 "2015",
                 "IMDb 6.5",
                 "https://goo.gl/AdMQnU",
                 "https://www.youtube.com/watch?v=1k59gXTWf-A")

movies = [bird, fig, forr, god, good, gua,
          inc, pulp, sch, shaw, godf, tom]

fresh_tomatoes.open_movies_page(movies)
