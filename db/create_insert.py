import sqlite3

def create_tables(db):
    with open('create.sql', 'r+') as sql_file:
        sql_script = sql_file.read()

    db = sqlite3.connect("animal_shelter.db")

    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    db.close()

def insert_dummy(db):
    with open('load.sql', 'r+') as sql_file:
        sql_script = sql_file.read()

    db = sqlite3.connect("animal_shelter.db")

    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    db.close()

db = sqlite3.connect("animal_shelter.db")
cursor = db.cursor()

create_tables(db)
insert_dummy(db)

for row in cursor.execute("SELECT * FROM vaccinations;"):
    print(row)