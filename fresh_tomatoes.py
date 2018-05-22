import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<html>
<head>
   <title>Movie Trailers</title>
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <script src = "https://code.jquery.com/jquery-1.12.3.min.js"
                integrity="sha256-aaODHAgvwQW1bFOGXMeX+pC4PZIPsvn2h1sArYOhgXQ="
                crossorigin="anonymous"></script>
        <link href = "https://fonts.googleapis.com/css?family=Courgette"
                    rel = "stylesheet">
        <link rel = "stylesheet"
                     href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <link href =
                       "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css"
                       rel = "stylesheet" type = "text/css" />
    <script src =
                 "https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js">
    </script>
    <script>
        $(document).ready(function () {
            $("#myVideo").on("hidden.bs.modal", function () {
                $("#myframeY").attr("src", "#");
            })
        })
        function changeVideo(id) {
            var iframe = document.getElementById("myframeY");
            iframe.src = "https://www.youtube.com/embed/" + id;
            $("#myVideo").modal("show");
         // Animate in the movies when the page loads
         $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
        }
    </script>
    <style>
        .container {
            flex-wrap: wrap;
            display: flex;
            flex: 10%;
            justify-content: center;
        }
        body {
            margin: 0;
            background-color: black;
        }
        #header {
            color: white;
            margin: 0px, 0px, 0px, 0px;
            text-align: center;
            font-size: 40px;
            font-family: 'georgia', serif;
        }
        img {
            height: 400px;
            width: 250px;
        }
        .im1{
            width: 50px;
            height: 50px;
            border-radius: 30px;
        }
        .im2{
            width: 50px;
            height: 50px;
            border-radius: 30px;
        }
        .mv:hover,
        .mv1:hover,
        .mv2:hover,
        .mv3:hover,
        .mv4:hover,
        .mv5:hover{
            background-color: white;
            visibility: visible;
            cursor: pointer;
        }
        .mv {
           height: auto;
           width: 300px;
           padding-left: 24px;
           padding-top: 20px;
           padding-bottom: 30px;
        }
        .mv1 {
            height: auto;
            width: 300px;
            padding-left: 24px;
            padding-top: 20px;
            padding-bottom: 30px;
        }
        .mv2 {
            height: auto;
            width: 300px;
            padding-left: 24px;
            padding-top: 20px;
            padding-bottom: 30px;
        }
        .mv3 {
            height: auto;
            width: 300px;
            padding-left: 24px;
            padding-top: 20px;
            padding-bottom: 30px;
        }
        .mv4 {
            height: auto;
            width: 300px;
            padding-left: 24px;
            padding-top: 20px;
            padding-bottom: 30px;
        }
        .mv5 {
           height: auto;
           width: 300px;
           padding-left: 24px;
           padding-top: 20px;
           padding-bottom: 30px;
        }
    </style>
</head>
    '''
# The main page layout and title bar
main_page_content = '''
 <body>
    <div id = "header">
            <img src =
                     "https://bit.ly/2s0HDPy"
                      alt = "logo" class = "im1"/>
                      MOVIE TRAILERS
                      <img src = "https://bit.ly/2s0HDPy"
                      alt = "logo" class = "im2"/></div>
    <main>
        <!-- Main Page Content -->
        <div class = "container">
            <div class = "mv" onclick = "changeVideo('gfgeIZyrIM0')">
                <img src = "https://bit.ly/2kcXyGQ" alt = "nemo">
                <figcaption style = "text-align: center; color: black;">
                    <b>Nemo</b>
                </figcaption>
            </div>
            <div class = "mv1" onclick = "changeVideo('IfePzXxIuvc')">
                <img src = "https://bit.ly/2KKiPTw" alt = "snowwhite">
                <figcaption style = "text-align: center; color:black;">
                    <b>Snow White</b>
                </figcaption>
            </div>
            <div class = "mv2" onclick = "changeVideo('WBYdp2sOut0')">
                <img src = "https://bit.ly/2kg3L59" alt = "tom&jerry">
                <figcaption style = "text-align: center; color: black;">
                    <B>Tom and Jerry</B>
                </figcaption>
            </div>
            <div class = "mv3" onclick  ="changeVideo('LKFuXETZUsI')">
                <img src = "https://bit.ly/2IU4RBt" alt = "Moana">
                <figcaption style = "text-align: center; color: black;">
                    <B>Moana</B>
                </figcaption>
            </div>
            <div class = "mv4" onclick = "changeVideo('ORFWdXl_zJ4')">
                <img src = "https://bit.ly/2s1R957" alt = "up">
                <figcaption style = "text-align: center; color:black;">
                    <b>UP</b>
                </figcaption>
            </div>
            <div class = "mv5" onclick = "changeVideo('eq-bqSvx0R8')">
                <img src = "https://bit.ly/2KKYrl8" alt = "cinderella">
                <figcaption style = "text-align: center; color: black;">
                    <b>Cinderella</b>
                </figcaption>
            </div>
        </div>
        <div class = "modal fade" id = "myVideo" tabindex="-1"
            role = "dialog" aria-labelledby = "myModalLabel">
            <div class = "modal-dialog" role = "document">
                <div class = "modal-content">
                    <div class = "modal-body">
                        <iframe id = "myframeY" width = "100%" height = "350px"
                          src = "" frameborder = "0" allowfullscreen></iframe>
                    </div>
                    <div class = "modal-footer">
                        <button type = "button" class = "btn btn-default"
                          data-dismiss = "modal">X</button>
                    </div>
                </div>
            </div>
        </div>
    </main>
</body>
</html>
'''
# A single movie entry html template
movie_title_content = '''
<div class = "col-md-6 col-lg-4 movie-title text-center" data-trailer-youtube-
id = "{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
   <img src="{poster_image_url}" width="220" height="342">
   <h2 style="color:white;">{movie_title}</h2>
</div>
'''


def create_movie_titles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or
        re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        # Append the tile for the movie with its content filled in
        content += movie_title_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
            )
        return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')
    """ Replace the placeholder for the movie
    tiles with the actual dynamically generated content """
    rendered_content = main_page_content.format(
        movie_titles=create_movie_titles_content(movies))
    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()
    # open the output file in the browser
    url = os.path.abspath(output_file.name)
    # open in a new tab, if possible
    webbrowser.open('file://' + url, new=2)


