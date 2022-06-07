from db.run_sql import run_sql

from models.album import Album
import repositories.artist_repository as artist_repository


def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist_id = row["artist_id"]
        artist = artist_repository.select(artist_id)
        album = Album(row["title"], row["genre"], artist, row["id"])
        albums.append(album)
    return albums


def save(album):
    sql = (
        "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING id"
    )
    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    album.id = id
    return album


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        artist_id = result["artist_id"]
        artist = artist_repository.select(artist_id)
        album = Album(result["title"], result["genre"], artist, result["id"])
    return album


def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values)
