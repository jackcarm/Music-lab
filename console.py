import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# album_repository.delete_all()
# artist_repository.delete_all()


artist_1 = Artist("Richard", "Ashcroft")
artist_repository.save(artist_1)

artist_2 = Artist("Bob", "Geldof")
artist_repository.save(artist_2)

artist_3 = Artist("Elton", "John")
artist_repository.save(artist_3)

artist_2 = Artist("Bob", "Dylan")
artist_repository.update(artist_2)

album_1 = Album("This is Rock", "Rock", artist_1)
album_repository.save(album_1)

album_2 = Album("This is classic", "Classis", artist_1)
album_repository.save(album_2)

album_3 = Album("This is Indie", "Indie", artist_3)
album_repository.save(album_3)

artist_2 = Artist("Bob", "Dylan")
artist_repository.update(artist_2)


pdb.set_trace()
