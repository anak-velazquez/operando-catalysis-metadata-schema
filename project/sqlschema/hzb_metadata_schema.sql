-- # Class: "chemical or drug or treatment" Description: ""
--     * Slot: id Description: 
-- # Class: "device" Description: "A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment"
--     * Slot: id Description: 
-- # Class: "catalysisSample" Description: "core parameters of a catalysis sample #metadata terms (parameters) are mapped to nfdi voc4cat"
--     * Slot: id Description: 
--     * Slot: sample_environment Description: 
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: vital_status Description: living or dead status
-- # Class: "sample" Description: "Represents a Sample"
--     * Slot: id Description: 
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: vital_status Description: living or dead status
--     * Slot: sampleCollection_id Description: Autocreated FK slot
-- # Class: "sampleCollection" Description: "A holder for Sample objects"
--     * Slot: id Description: 
-- # Class: "entity" Description: "Root Biolink Model class for all things and informational relationships, real or imagined."
--     * Slot: id Description: 
-- # Class: "namedThing" Description: "a databased entity or concept/class"
--     * Slot: id Description: 

CREATE TABLE "chemical or drug or treatment" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE device (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "catalysisSample" (
	id INTEGER NOT NULL, 
	sample_environment TEXT, 
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	vital_status VARCHAR(7), 
	PRIMARY KEY (id)
);
CREATE TABLE "sampleCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE entity (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "namedThing" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE sample (
	id INTEGER NOT NULL, 
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	vital_status VARCHAR(7), 
	"sampleCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("sampleCollection_id") REFERENCES "sampleCollection" (id)
);