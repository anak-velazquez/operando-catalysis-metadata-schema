-- # Class: "chemical or drug or treatment" Description: ""
--     * Slot: id Description: 
-- # Class: "Entity" Description: "An entity is anything that exists or has existed or will exist.  Model class for all things and informational relationships, real or imagined."
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "NamedEntity" Description: "a databased entity or concept/class"
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "DataCite" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Person" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Project" Description: "lorem"
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Device" Description: "A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment"
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Sample" Description: "Information about a generic laboratory sample, discipline agnostic."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: SampleCollection_id Description: Autocreated FK slot
-- # Class: "SampleCollection" Description: "A holder for Sample objects"
--     * Slot: id Description: 
-- # Class: "Scientist" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "CatalysisSample" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: CatalysisSampleCollection_id Description: Autocreated FK slot
-- # Class: "Catalyst" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "ThinFilmCatalyst" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "PowderCatalyst" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Recipe" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Mixture" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Workflow" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Process" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Experiment" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Measurement" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Parameter" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Reaction" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "ReactionProduct" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: ReactionProductCollection_id Description: Autocreated FK slot
-- # Class: "Reactor" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "CatalysisSampleCollection" Description: "A holder for CatalysisSample objects"
--     * Slot: id Description: 
-- # Class: "ReactionProductCollection" Description: "A holder for ReactionProduct objects"
--     * Slot: id Description: 
-- # Class: "Beamline" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "BeamlineExperiment" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "BeamlineScientist" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "mySpot" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "EMIL_Pink" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "EMIL_OAESE" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "SampleEnvironment" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "SamplePositioning" Description: "A person (alive, dead, undead, or fictional)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Person_has_employment_history" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: has_employment_history Description: 
-- # Class: "Scientist_has_employment_history" Description: ""
--     * Slot: Scientist_id Description: Autocreated FK slot
--     * Slot: has_employment_history Description: 
-- # Class: "BeamlineScientist_has_employment_history" Description: ""
--     * Slot: BeamlineScientist_id Description: Autocreated FK slot
--     * Slot: has_employment_history Description: 

CREATE TABLE "chemical or drug or treatment" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Entity" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "NamedEntity" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataCite" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	gender VARCHAR(9), 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Project" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Device" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SampleCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Scientist" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	gender VARCHAR(9), 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Catalyst" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "ThinFilmCatalyst" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "PowderCatalyst" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Recipe" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Mixture" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Workflow" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Process" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Experiment" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Measurement" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Parameter" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Reaction" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Reactor" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CatalysisSampleCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ReactionProductCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Beamline" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "BeamlineExperiment" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "BeamlineScientist" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	gender VARCHAR(9), 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "mySpot" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EMIL_Pink" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EMIL_OAESE" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SampleEnvironment" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SamplePositioning" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sample" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	"SampleCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("SampleCollection_id") REFERENCES "SampleCollection" (id)
);
CREATE TABLE "CatalysisSample" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	"CatalysisSampleCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("CatalysisSampleCollection_id") REFERENCES "CatalysisSampleCollection" (id)
);
CREATE TABLE "ReactionProduct" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	"ReactionProductCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ReactionProductCollection_id") REFERENCES "ReactionProductCollection" (id)
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
CREATE TABLE "BeamlineScientist_has_employment_history" (
	"BeamlineScientist_id" TEXT, 
	has_employment_history TEXT, 
	PRIMARY KEY ("BeamlineScientist_id", has_employment_history), 
	FOREIGN KEY("BeamlineScientist_id") REFERENCES "BeamlineScientist" (id)
);