from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

class ReusableForm(Form):
	'''
	Form to perform the search functionality
	in the /search route where one needs to
	type in the first and last name
	'''
	firstname = TextField('Firstname:', validators=[validators.DataRequired()])

class LoginForm(Form):
	email = TextField('Email', validators=[validators.DataRequired()])
	password = TextField('Password', validators=[validators.DataRequired()])

class UpdateForm(Form):
	#update = TextField('How do you want to modify your experience?', validators=[validators.DataRequired()])
	name = TextField('Name:', validators=[validators.DataRequired()])
	species = TextField('Species:', validators=[validators.DataRequired()])
	pri_col = TextField('Primary Color:', validators=[validators.DataRequired()])
	chip_id = TextField('Implant ChipID:', validators=[validators.DataRequired()])
	breed = TextField('Breed:', validators=[validators.DataRequired()])
	gender = TextField('Gender:', validators=[validators.DataRequired()])
	dob = TextField('Year of Birth:', validators=[validators.DataRequired()])
	pattern = TextField('Pattern:', validators=[validators.DataRequired()])
	adm_year = TextField('Admission Year:', validators=[validators.DataRequired()])

class UpdateAnimalNameForm(Form):
	chip_id = TextField('Implant ChipID:', validators=[validators.DataRequired()])
	name = TextField('Name:', validators=[validators.DataRequired()])

class DeleteAnimalForm(Form):
	chip_id = TextField('Implant ChipID:', validators=[validators.DataRequired()])





