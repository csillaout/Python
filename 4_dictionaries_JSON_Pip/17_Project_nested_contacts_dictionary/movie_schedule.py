current_movies = {'The Grinch': '11:00am', 'Rudolf': '1:00pm', 'Frotsy the Snowman': '3:00pm', 'Christmas Vacation': ' 5:00pm'}

print('We are showing the following movies:')
for key in current_movies:
    print(key)

movie = input('What movie wold you like the showtime for?\n')
showtime = current_movies.get(movie)

if showtime ==None:
    print("Requested movie isnt playing")
else:
    print(movie, "is playing a", showtime)

