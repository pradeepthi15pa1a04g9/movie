#!/usr/bin/env python
print("content-type:text/html \n")
import media
import fresh_tomatoes

nemo= media.Movie("nemo","finding nemo","http://www.weaverstreetmarket.coop/wp-content/uploads/2016/06/movie-poster-nemo.jpeg",
                    "https://www.youtube.com/embed/gfgeIZyrIM0")
sw=media.Movie("snowwhite","about a girl","https://image.tmdb.org/t/p/w185/wbVGRBYPRRahIZNGXY9TfHDUSc2.jpg"
                ,"https://www.youtube.com/embed/IfePzXxIuvc")
tj=media.Movie("tom&jerry","Tom&Jerry","https://upload.wikimedia.org/wikipedia/en/b/b4/Tom_and_Jerry_-_The_Movie_Poster.png","https://www.youtube.com/embed/WBYdp2sOut0")
moana=media.Movie("moana","saving island","https://cdn.disneymovieclub.go.com/static/Catalog/Acquisition_Agnostic_191x269/Moana_Acq.jpg"
                 ,"https://www.youtube.com/embed/LKFuXETZUsI")
up=media.Movie("up","adventures","https://www.cardiffboxoffice.com/asset/Event/11505/up.jpg","https://www.youtube.com/embed/ORFWdXl_zJ4")
cinderella=media.Movie("cinderella","cinderella","https://www.columbiaassociation.org/wp-content/uploads/2016/03/ShowImage-id=10603&t=635689308124800000.jpeg"
                                ,"https://www.youtube.com/embed/eq-bqSvx0R8")
                              

movies = [nemo,sw,tj,moana,up,cinderella]
fresh_tomatoes.open_movies_page(movies)
