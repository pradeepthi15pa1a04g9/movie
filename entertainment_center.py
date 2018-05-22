import media
import fresh_tomatoes

# New movie object.
nemo = media.Movie("nemo", "finding nemo", "https://bit.ly/2kcXyGQ",
                   "https://www.youtube.com/embed/gfgeIZyrIM0")
# New movie object.
snowwhite = media.Movie("snowwhite", "about a girl", "https://bit.ly/2KKiPTw",
                        "https://www.youtube.com/embed/IfePzXxIuvc")
# New movie object.
tomandjerry = media.Movie("tomandjerry", "tomandjerry", "https://bit.ly/2kg3L59",
                        "https://www.youtube.com/embed/WBYdp2sOut0")
# New movie object.
moana = media.Movie("moana", "saving island", "https://bit.ly/2IU4RBt",
                    "https://www.youtube.com/embed/LKFuXETZUsI")
# New movie object.
up = media.Movie("up", "adventures", "https://bit.ly/2s1R957",
                 "https://www.youtube.com/embed/ORFWdXl_zJ4")
# New movie object.
cinderella = media.Movie("cinderella", "cinderella", "https://bit.ly/2KKYrl8",
                         "https://www.youtube.com/embed/eq-bqSvx0R8")
# Array with all movies
movies = [nemo, snowwhite, tomandjerry, moana, up, cinderella]
# Call the function open movie page from the file fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
