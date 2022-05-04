import os
import logging
from forms import *
from db.funcs import *
from pathlib import Path  # python3 only
#from flaskext.mysql import *
from dotenv import load_dotenv
from flask import Flask, render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#import sqlite3
import psycopg2


DEBUG = True
# Load the secrets from the '.secrets' file
env_path = Path('.') / '.secrets'	
load_dotenv(dotenv_path=env_path, verbose=DEBUG)

app = Flask(__name__)	#initialising flask
app.config.from_object(__name__)	#configuring flask
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


logging.basicConfig(filename='usage.log',level=logging.DEBUG)

is_user_active = False


@app.route("/", methods=['GET', 'POST'])
def index():
	'''
	The root route, i.e. the landing page
	'''

	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")
	cursor = db.cursor()

	cursor.execute("SELECT COUNT(*) FROM animals;")
	count_animals = cursor.fetchall()[0][0]

	cursor.execute("SELECT species, COUNT(*) FROM animals GROUP BY species;")
	count_by_species = cursor.fetchall()
	return render_template("index.html", count_animals=count_animals, count_by_species=count_by_species)	#render_template basically renders the html code of page mentioned as arg when needed

@app.route("/animal-vaccine-status", methods=['GET', 'POST'])
def search():
	'''
	The route to search for specific people.
	One can give a particular firstname and
	lastname and we return all people whose
	first and lastnames match with the name
	entered by the user in the /search form.
	'''
	form = ReusableForm(request.form)	#Creating a form object
	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")
	#db = sqlite3.connect("db/animal_shelter.db")

	cursor = db.cursor()

	cursor.execute("SELECT COUNT(*) FROM vaccinations;")
	vaccines_dispersed = cursor.fetchall()
	vaccines_dispersed = vaccines_dispersed[0][0]
	
	if(request.method == 'POST'):		#If the user submits data in the Form
		if(form.validate()):		#If form is validated
			name = request.form['firstname']	#Get firstname
			data = search_vaccine_status_by_name(cursor, name)	#Search DB for given first and lastname

			if(str(data) != "()"):	#Check if null tuple
				return render_template("search.html", vaccines_dispersed=vaccines_dispersed, form=form, batch_list=data)	#Pass data if not null tuple
			else:	#if null tuple, pass the string format of null tuple --> "()"
				return render_template("search.html", vaccines_dispersed=vaccines_dispersed, form=form, batch_list="()")
	return render_template("search.html", form=form, vaccines_dispersed=vaccines_dispersed)

@app.route("/alumni")
def alumni():
	'''
	The route, in local hosting case,
	"localhost:5000/alumni" is displayed.
	The alumni.html page is rendered here.
	'''
	return render_template("alumni.html")


@app.route("/adoptions")
def adoptions():
	#db = sqlite3.connect("db/animal_shelter.db")
	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")

	cursor = db.cursor()

	data = get_adoptions(cursor)
	#print(data[1])

	return render_template("adoptions.html", data=data)

@app.route("/animals")
def animals():
	#db = sqlite3.connect("db/animal_shelter.db")
	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")

	cursor = db.cursor()

	data = get_animals(cursor)
	#print(data[1])

	return render_template("animals.html", data=data)

@app.route("/species")
def species():
	
	#db = sqlite3.connect("db/animal_shelter.db")
	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")

	cursor = db.cursor()


	data = get_species(cursor)
	#print(data[1])

	return render_template("species.html", data=data)

@app.route("/staff")
def staff():
	#db = sqlite3.connect("db/animal_shelter.db")
	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")

	cursor = db.cursor()

	data = get_staff(cursor)

	new_data = []
	for staff in data:
		new_data += [staff + tuple((staff[0].split("@"))[0].split("."))]
	print(new_data)

	return render_template("staff.html", data=new_data)

@app.route("/animal/<string:name>")
def individual_page(name):
	'''
	This is an individual_page for everyone.
	Contets change depending on the name of
	student that one clicks on.
	Example of route : /alumni/2020/XYZ-ABC, /alumni/2019/XYZ-ABC
	In both cases, XYZ, ABC are firstname and lastname respectively
	and the batch is 2020 and 2019 respectively.

	batch, firstname and lastname are vars here
	and change depending on where they are clicked
	from and when they are clicked.
	'''
	#db = sqlite3.connect("db/animal_shelter.db")
	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")

	cursor = db.cursor()

	data = get_animal_details_by_name(cursor, name)
	#print(data[1])

	return render_template("individual_page.html", name=name, details=data)

@app.route("/update-experience", methods=['GET','POST'])
def update_experience():
	form = UpdateForm(request.form)	#Creating a form object
	#db = sqlite3.connect("db/animal_shelter.db")
	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")

	cursor = db.cursor()
	
	if(request.method == 'POST'):		#If the user submits data in the Form
		if(form.validate()):		#If form is validated
			name = request.form['name']
			species = request.form['species']
			pri_col = request.form['pri_col']
			chip_id = request.form['chip_id']
			breed = request.form['breed']
			gender = request.form['gender']
			dob = request.form['dob']
			pattern = request.form['pattern']
			adm_year = request.form['adm_year']	

			cursor.execute("SELECT * FROM colors;")
			colors = cursor.fetchall()
			colors = [entry[0] for entry in colors]

			cursor.execute("SELECT * FROM species;")
			species_list = cursor.fetchall()
			species_list = [entry[0] for entry in species]
			print(colors)

			try:
				if(pri_col in colors):
					if(species in species_list):
						update_exp(db, cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)
						print(cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)
						return redirect(url_for("index"))
					else:
						update_species(db, cursor, species)
						update_exp(db, cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)

						print(cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)
						return redirect(url_for("index"))
				else:
					update_color(db, cursor, pri_col)
					if(species in species_list):
						update_exp(db, cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)
						print(cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)
						return redirect(url_for("index"))
					else:
						update_species(db, cursor, species)
						update_exp(db, cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)

						print(cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)
						return redirect(url_for("index"))
				#update_exp(db, cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)
				#print(cursor, name, species, pri_col, chip_id, breed, gender, dob, pattern, adm_year)
				#return render_template("index.html")

				
			except psycopg2.errors.UniqueViolation:
				return render_template("insert_error.html")
			

	return render_template("update_experience.html", form=form)

@app.route("/update-animal-single", methods=['GET','POST'])
def update_animal_single():
	form = UpdateAnimalNameForm(request.form)	#Creating a form object
	#db = sqlite3.connect("db/animal_shelter.db")
	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")

	cursor = db.cursor()
	
	if(request.method == 'POST'):		#If the user submits data in the Form
		if(form.validate()):		#If form is validated
			name = request.form['name']
			chip_id = request.form['chip_id']

			update_single_animal(db, cursor, name, chip_id)
			return redirect(url_for("index"))

	return render_template("update_animal_single.html", form=form)

@app.route("/delete-animal", methods=['GET','POST'])
def delete_animal():
	form = DeleteAnimalForm(request.form)	#Creating a form object

	db = psycopg2.connect(database = "Animal_Shelter", user = "postgres", password = "123456", host = "127.0.0.1", port = "5434")

	cursor = db.cursor()
	
	if(request.method == 'POST'):		#If the user submits data in the Form
		if(form.validate()):		#If form is validated
			chip_id = request.form['chip_id']

			delete_single_animal(db, cursor, chip_id)
			return redirect(url_for("index"))

	return render_template("delete_animal_single.html", form=form)




@app.errorhandler(404)
def not_found(e):
	'''
	Error message displayed if Page
	not found or user tries accessing
	a page that doesn't exist or have access to
	'''
	return render_template("404.html")


@app.errorhandler(500)
def application_error(e):
	'''
	Error handler for unexpected errors.
	'''
	return 'Sorry, unexpected error: {}'.format(e), 500


if(__name__ == "__main__"):
	app.run(host="localhost", port=8000)
