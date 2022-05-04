'''def fetch_names(cursor, batch):
	
	Function that gets firstname and
	lastname of all students from a
	particular batch for alumni_batch.html
	page in the templates folder.

	## ABOUT THE ARGS ##
	cursor : To establish connection with tables
	batch : To query in database with batch
	
	data_temp = cursor.execute("SELECT Fname, Lname from Details where Batch='" + batch + "\' ORDER BY Fname;")	#change to batch instead of branch
	data = cursor.fetchall()
	print(data)
	return data

def get_individual_data(cursor, firstname, lastname, batch):
	
	Function that gets experience of a
	student from a particular batch for
	individual_page.html in templates folder.

	## ABOUT THE ARGS ##
	cursor : To establish connection with tables
	firstname : To query in db with firstname
	lastname : To query in db with lastname
	batch : To query in database with batch

	Returns experience of the students whose
	firstname, lastname and batch match.
	
	#print("SELECT exp from temp where (fname='" + firstname + "', lname='" + lastname + "', batch=" + batch + ");")
	rollno = get_rollno(cursor, firstname, lastname, batch)
	data_temp = cursor.execute("SELECT experiance from Exp where Rollno=" + rollno + ";")	#change to batch instead of branch
	data = cursor.fetchall()
	print(data)
	return data

def search_by_name(cursor, firstname):
	
	Gets the firstname, lastname and batch
	from the table temp given a firstname and
	lastname in the /search route.

	Returns all fields that match the given
	first and lastname by the user.
	
	data_temp = cursor.execute("SELECT Fname, Lname, Batch from Details where (fname='" + firstname + "' and lname='" + lastname + "');")	#change to batch instead of branch
	data = cursor.fetchall()
	print(data)
	return data

def update_exp(cursor, experience, firstname, lastname, batch):
	rollno = get_rollno(cursor, firstname, lastname, batch)
	data_temp = cursor.execute("UPDATE Exp SET experiance='" + experience + "' where Rollno=" + rollno + ";")
	conn.autocommit = True
	data = cursor.fetchall()
	print(data)

def update_contact(cursor, email, firstname, lastname, batch):
	rollno = get_rollno(cursor, firstname, lastname, batch)
	data_temp = cursor.execute("UPDATE Contact_Details SET EmailID='" + email + "' where Rollno=" + rollno + ";")
	conn.autocommit = True
	data = cursor.fetchall()
	print(data)

def update_location(cursor, location, firstname, lastname, batch):
	rollno = get_rollno(cursor, firstname, lastname, batch)
	data_temp = cursor.execute("UPDATE Current_Location SET Location='" + location + "' where Rollno=" + rollno + ";")
	conn.autocommit = True
	data = cursor.fetchall()
	print(data)

def get_loc(cursor,firstname, lastname, batch):
	rollno = get_rollno(cursor, firstname, lastname, batch)
	data_temp = cursor.execute("SELECT Location from Current_Location where Rollno=" + rollno + ";")
	data = cursor.fetchall()
	print(data)
	return data

def get_email(cursor, firstname, lastname, batch):
	rollno = get_rollno(cursor, firstname, lastname, batch)
	data_temp = cursor.execute("SELECT EmailID from Contact_Details where Rollno=" + rollno + ";")
	data = cursor.fetchall()
	print(data[0][0])
	return data[0][0]


def get_rollno(cursor, firstname, lastname, batch):
	print("in here")
	data_temp = cursor.execute("SELECT Rollno from Details where (Fname='" + firstname + "' and Lname='" + lastname + "' and Batch=" + batch + ");")
	data = cursor.fetchall()
	print(data[0][0])
	return data[0][0]'''

def search_vaccine_status_by_name(cursor, name):
	cursor.execute("SELECT name, species, vaccination_time, vaccine, batch FROM vaccinations WHERE name='" + name + "';")
	data = cursor.fetchall()
	#data.fetchall()
	print(data)
	return data

def get_animal_details_by_name(cursor, name):
	cursor.execute("SELECT species, primary_color, gender, birth_date, admission_date FROM animals WHERE name='" + name + "';")
	data = cursor.fetchall()
	print(data)
	return data

def get_adoptions(cursor):
	cursor.execute("SELECT * FROM adoptions;")
	data = cursor.fetchall()
	print(data)
	return data

def get_species(cursor):
	cursor.execute("SELECT * FROM species;")
	data = cursor.fetchall()
	print(data)
	return data

def get_staff(cursor):
	cursor.execute("SELECT * FROM staff;")
	data = cursor.fetchall()
	print(data)
	return data

def get_animals(cursor):
	cursor.execute("SELECT * FROM animals;")
	data = cursor.fetchall()
	print(data)
	return data

def update_exp(db, cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year):
	#statement = "INSERT INTO animals(name, species, primary_color, implant_chip_id, breed, gender, birth_date, pattern, admission_date) VALUES(?,?,?,?,?,?,?,?,?);"
	statement = "INSERT INTO animals(name, species, primary_color, implant_chip_id, breed, gender, birth_date, pattern, admission_date) VALUES('" + str(name) + "','" + str(species) + "','" + str(pri_col) + "','" + str(chip_id) + "','" + str(breed) + "','" + str(gender) + "','" + str(dob) + "','" + str(pattern) + "','" + str(adm_year) + "');"

	cursor.execute(statement, (name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year))
	db.commit()
	#cursor.execute("SELECT * FROM animals;")
	return cursor.lastrowid

def update_color(db, cursor, color):
	#statement = "INSERT INTO animals(name, species, primary_color, implant_chip_id, breed, gender, birth_date, pattern, admission_date) VALUES(?,?,?,?,?,?,?,?,?);"
	statement = "INSERT INTO colors(color) VALUES('" + str(color) + "');"

	cursor.execute(statement)
	db.commit()
	#cursor.execute("SELECT * FROM animals;")
	return cursor.lastrowid

def update_species(db, cursor, species):
	#statement = "INSERT INTO animals(name, species, primary_color, implant_chip_id, breed, gender, birth_date, pattern, admission_date) VALUES(?,?,?,?,?,?,?,?,?);"
	statement = "INSERT INTO species(species) VALUES('" + str(species) + "');"

	cursor.execute(statement)
	db.commit()
	#cursor.execute("SELECT * FROM animals;")
	return cursor.lastrowid

def update_single_animal(db, cursor, name, chip_id):
	statement = "UPDATE animals SET name ='" + name + "' WHERE implant_chip_id='" + chip_id + "';"
	cursor.execute(statement)
	db.commit()
	return cursor.lastrowid

def delete_single_animal(db, cursor, chip_id):
	statement = "DELETE FROM animals WHERE implant_chip_id='" + chip_id + "';"
	cursor.execute(statement)
	db.commit()
	return cursor.lastrowid




