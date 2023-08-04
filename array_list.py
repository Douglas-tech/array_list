# Define class
class Album:
    def __init__(self, albumName, numberOfSongs, albumArtist):
        self.albumName = albumName
        self.numberOfSongs = numberOfSongs
        self.albumArtist = albumArtist

    def __str__(self):
        return f"({self.albumName}, {self.albumArtist}, {self.numberOfSongs})"


# Create a new list called albums1 and add 5 albums to it
albums1 = [
    Album("Thriller", 9, "Michael Jackson"),
    Album("Abbey Road", 17, "The Beatles"),
    Album("The Dark Side of the Moon", 10, "Pink Floyd"),
    Album("Born to Run", 8, "Bruce Springsteen"),
    Album("Hotel California", 9, "Eagles"),
]

# Print albums1
print("Albums1:")
for album in albums1:
    print(album)

# Sort the list according to the numberOfSongs
albums1.sort(key=lambda album: album.numberOfSongs)

# Print sorted albums1
print("\nSorted Albums1:")
for album in albums1:
    print(album)

# Swap the elements at position 1 and 2 in albums1
albums1[1], albums1[2] = albums1[2], albums1[1]

# Print albums1 after swapping
print("\nAlbums1 after swapping:")
for album in albums1:
    print(album)

# Create a new list called albums2 and add 5 albums to it
albums2 = [
    Album("Back in Black", 10, "AC/DC"),
    Album("Rumours", 11, "Fleetwood Mac"),
    Album("Purple Rain", 9, "Prince"),
    Album("Nevermind", 12, "Nirvana"),
    Album("The Joshua Tree", 11, "U2")
]

# Print albums2
print("\nAlbums2:")
for album in albums2:
    print(album)

# Copy all albums from albums1 into albums2
albums2.extend(albums1)

# Add two new albums to albums2
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Oops!... I Did It Again", 16, "Britney Spears"))

# Sort albums2 alphabetically by album name
albums2.sort(key=lambda album: album.albumName)

# Print sorted albums2
print("\nSorted Albums2:")
for album in albums2:
    print(album)

# Search for the album "Dark Side of the Moon" in albums2 and print its index
album_name = "Dark Side of the Moon"
index = -1
for i, album in enumerate(albums2):
    if album.albumName == album_name:
        index = i
        break

print(f"\nIndex of '{album_name}' in Albums2: {index}")