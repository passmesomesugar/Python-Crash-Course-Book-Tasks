# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.
def make_album(artist, title, number_of_songs=None):
    music_album = {'artist': artist, 'title': title}
    if number_of_songs:
        music_album['number_of_songs'] = number_of_songs
    return music_album


while True:
    print("Enter album data")
    print("q to quit")
    artist = input("Artist: ")
    if artist == 'q':
        break
    title = input("Album title: ")
    if title == 'q':
        break
    number = input("Number of songs: ")
    if number == 'q':
        break
    new_album = make_album(artist, title, number_of_songs=number)

print(new_album)
