from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


album1 = Album("Bob Marley And The Wailers", "Reggae","Bob Marley")
album_repository.save(album1)

artist1 = Artist("Sinach")
artist_repository.save(artist1)

album2 = Album("Get rich or die trying", "hip hop","50 cent")
album_repository.save(album2)

artist2 = Artist("Kanye West")
artist_repository.save(artist2)