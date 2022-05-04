------------------------------------
-- Team Name: Ace Dominators III ---
-- Create Tables SQL File ----------
------------------------------------

-- Create Database

-- Create Colors table
CREATE	TABLE Colors
(
	Color VARCHAR(10) NOT NULL 
		PRIMARY KEY
);

-- Create Species table
CREATE TABLE Species 
(
	Species VARCHAR(10) NOT NULL 
		PRIMARY KEY
);

-- Create Animals table
CREATE	TABLE Animals
(
	Name			VARCHAR(20)			NOT NULL,
	Species			VARCHAR(10)			NOT NULL
		REFERENCES Species (Species),
	Primary_Color	VARCHAR(10)			NOT NULL
		REFERENCES Colors (Color),
	Implant_Chip_ID	VARCHAR(50)			NOT NULL
		UNIQUE,
	Breed			VARCHAR(50)			NULL,
	Gender			CHAR(1)				NOT NULL
		CHECK (Gender IN ('F', 'M')),
	Birth_Date		DATE				NOT NULL,
	Pattern			VARCHAR(20)			NOT NULL,
	Admission_Date	DATE				NOT NULL,
	PRIMARY KEY (Name, Species)
);

-- Create Persons table
CREATE	TABLE Persons
(
	Email		VARCHAR(100)	NOT NULL 
		PRIMARY KEY,
	First_Name	VARCHAR(15)		NOT NULL,
	Last_Name	VARCHAR(15)		NOT NULL,
	Birth_Date	DATE			NULL,
	Address		VARCHAR(100)	NOT NULL,
	State		VARCHAR(20)		NOT NULL,
	City		VARCHAR(30)		NOT NULL,
	Zip_Code	CHAR(5)			NOT NULL
);

-- Create Staff table
CREATE	TABLE Staff
(
	Email	VARCHAR(100)	NOT NULL 
		PRIMARY KEY
		REFERENCES Persons(Email), 
	Hire_Date DATE			NOT NULL
);

-- Create Staff_Roles table
CREATE	TABLE Staff_Roles 
(
	Role VARCHAR(20) NOT NULL PRIMARY KEY 
);

-- Create Staff_Assignments table
CREATE TABLE Staff_Assignments
(
	Email		VARCHAR(100)	NOT NULL
		REFERENCES Staff (Email) ON UPDATE CASCADE,
	Role		VARCHAR(20)		NOT NULL
		REFERENCES Staff_Roles (Role),
	Assigned	DATE			NOT NULL,
	PRIMARY KEY (Email, Role)
);

-- Create Adoptions table
CREATE	TABLE Adoptions
(
	Name			VARCHAR(20)		NOT NULL,
	Species			VARCHAR(10)		NOT NULL,
	Adopter_Email	VARCHAR(100)	NOT NULL
		REFERENCES Persons (Email) ON UPDATE CASCADE,
	Adoption_Date	DATE			NOT NULL,
	Adoption_Fee	SMALLINT		NOT NULL
		CHECK (Adoption_Fee >= (0)),
	PRIMARY KEY (Name, Species, Adopter_Email),
	FOREIGN KEY (Name, Species)
		REFERENCES Animals (Name, Species) ON UPDATE CASCADE
);

-- Create Vaccinations table
CREATE TABLE Vaccinations
(
	Name				VARCHAR(20)		NOT NULL,
	Species				VARCHAR(10)		NOT NULL,
	Vaccination_Time	TIMESTAMP		NOT NULL,
	Vaccine				VARCHAR(50)		NOT NULL,
	Batch				VARCHAR(20)		NOT NULL,
	Comments			VARCHAR(500)	NULL,
	Email				VARCHAR(100)	NOT NULL
		REFERENCES Staff (Email) ON UPDATE CASCADE,
	PRIMARY KEY (Name, Species, Vaccine, Vaccination_Time),
	FOREIGN KEY (Name, Species)
		REFERENCES Animals (Name, Species)
);

