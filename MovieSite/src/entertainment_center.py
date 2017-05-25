import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","Story of a boy and his toys that come to life.", "https://en.wikipedia.org/wiki/File:Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "Ferngully in space", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")
school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?/v=3PsUJFEBC74")
ratatouille = media.Movie("Ratatouille", "A rat is a chef in paris", "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", "https://www.youtube.com/watch?v=c3sBBRxDAqk")
midnight_in_paris = media.Movie("Midnight in paris", "Going back in time to meet authors", "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", "https://www.youtube.com/watch?v=FAfR8omt-CY")
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris]
fresh_tomatoes.open_movies_page(movies)
# print(toy_story.storyline)
# toy_story.show_trailer()
# print(avatar.storyline)