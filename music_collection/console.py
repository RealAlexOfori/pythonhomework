from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


artist1 = Artist("Bob Marley")
artist_repository.save(artist1)

artist2 = Artist("Kanye West")
artist_repository.save(artist2)

album1 = Album("Bob Marley And The Wailers", "Reggae", artist1)
album_repository.save(album1)

album2 = Album("Get rich or die trying", "hip hop", artist2)
album_repository.save(album2)

all_albums = album_repository.select_all()


for album in all_albums:
    print(album.name + ": " + album.artist.name)


