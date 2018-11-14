fron sqlite3 import connect

database= connect('дорп.db')

database.execute(
    "INSERT INTO persons VALUES('John Dow', 42, 'loafer')"
)