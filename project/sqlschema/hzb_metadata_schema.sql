-- # Class: "chemical or drug or treatment" Description: ""
--     * Slot: id Description: 
-- # Class: "Person" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "Scientist" Description: "A scientist (alive, dead, undead, or fictional)."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "device" Description: "A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "CatalysisSample" Description: "core parameters of a catalysis sample #metadata terms (parameters) are mapped to nfdi voc4cat"
--     * Slot: sample_environment Description: 
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: vital_status Description: living or dead status
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "Sample" Description: "Represents a Sample"
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: vital_status Description: living or dead status
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: SampleCollection_id Description: Autocreated FK slot
-- # Class: "SampleCollection" Description: "A holder for Sample objects"
--     * Slot: id Description: 
-- # Class: "Experiment" Description: "something following a protocol?"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "Rockit_experiment" Description: "describing the standard setup for ROCK-IT beamline experiment. Sonal + Ana"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "BESSY" Description: "Sonal"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "Myspot_Beamline" Description: "Sonal"
--     * Slot: type Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "Beamline" Description: "Sonal"
--     * Slot: type Description: 
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "BeamlineExperiment" Description: "Sonal"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "Organization" Description: ""
--     * Slot: id Description: 
--     * Slot: name Description: 
--     * Slot: type Description: 
-- # Class: "Entity" Description: "An entity is anything that exists or has existed or will exist.  Model class for all things and informational relationships, real or imagined."
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "NamedThing" Description: "a databased entity or concept/class"
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "Person_has_employment_history" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: has_employment_history Description: 
-- # Class: "Scientist_has_employment_history" Description: ""
--     * Slot: Scientist_id Description: Autocreated FK slot
--     * Slot: has_employment_history Description: 

CREATE TABLE "chemical or drug or treatment" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	gender VARCHAR(9), 
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Scientist" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	gender VARCHAR(9), 
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE device (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CatalysisSample" (
	sample_environment TEXT, 
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	vital_status VARCHAR(7), 
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SampleCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Experiment" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Rockit_experiment" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "BESSY" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Myspot_Beamline" (
	type TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Beamline" (
	type TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "BeamlineExperiment" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Organization" (
	id INTEGER NOT NULL, 
	name TEXT, 
	type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Entity" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sample" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	vital_status VARCHAR(7), 
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	"SampleCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("SampleCollection_id") REFERENCES "SampleCollection" (id)
);
CREATE TABLE "Person_has_employment_history" (
	"Person_id" TEXT, 
	has_employment_history TEXT, 
	PRIMARY KEY ("Person_id", has_employment_history), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);
CREATE TABLE "Scientist_has_employment_history" (
	"Scientist_id" TEXT, 
	has_employment_history TEXT, 
	PRIMARY KEY ("Scientist_id", has_employment_history), 
	FOREIGN KEY("Scientist_id") REFERENCES "Scientist" (id)
);