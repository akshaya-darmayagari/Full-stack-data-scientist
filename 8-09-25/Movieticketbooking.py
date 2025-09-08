class Cinema:
    def __init__(self, movies):
        self.movies=movies
    def book(self,movie,seats):
        if self.movies[movie]>=seats:
            self.movies[movie]-=seats
            return f"Booked {seats} tickets for {movie}"
        else:
            return "Not enough seats available"
    def cancel(self,movie,seats):
        self.movies[movie]+=seats
        return f"Cancelled {seats} ticket for {movie}"
    def show_movies(self):
        return "Movies: "+str(self.movies)
cinema=Cinema({"Avatar": 10, "Batman": 5})
print(cinema.book("Avatar", 2))
print(cinema.cancel("Avatar", 1))
print(cinema.show_movies())