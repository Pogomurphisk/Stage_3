import media
import fresh_tomatoes

con_air = media.Movie("Con Air", 
	"https://upload.wikimedia.org/wikipedia/en/1/1d/Conairinternational.jpg",
	"https://www.youtube.com/watch?v=fWq-S1_1vnc")

the_rock = media.Movie("The Rock",
	"https://upload.wikimedia.org/wikipedia/en/8/82/The_Rock_%28movie%29.jpg",
	"https://www.youtube.com/watch?v=UWfXyNfVotg")

face_off = media.Movie("Face/Off",
	"https://upload.wikimedia.org/wikipedia/en/0/0c/FaceOff_%281997_film%29_poster.jpg",
	"https://www.youtube.com/watch?v=3zebJ_NoduE")

kick_ass = media.Movie("Kick-Ass",
	"https://upload.wikimedia.org/wikipedia/en/3/30/Kick-Ass_film_poster.jpg",
	"https://www.youtube.com/watch?v=rFpWpkxsVI8")

movies = [con_air, the_rock, face_off, kick_ass]
fresh_tomatoes.open_movies_page(movies)