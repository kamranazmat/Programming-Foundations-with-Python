import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
						"A story of a boy and his toys that come to life", 
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", 
						"A marine on an alien planet", 
						"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", 
						"https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#print (toy_story.storyline)
#print (avatar.storyline)
#avatar.show_trailer()
movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)

#Predefined Class Attributes
print (media.Movie.__name__)
print (media.Movie.__module__)
print (media.Movie.__doc__)
print (media.Movie.__dict__)

#avatar.sample()