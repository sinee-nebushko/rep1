from sqlite3 import connect

database = connect('дорп.db')

database.execute(
    "INSERT INTO persons VALUES('elisabeth', 98, 'queen')"
    "INSERT INTO persons VALUES('elisabeth', 98, 'queen')"
)

database.commit()