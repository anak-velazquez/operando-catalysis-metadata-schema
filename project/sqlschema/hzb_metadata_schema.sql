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
-- # Class: "DataCite" Description: "Represents metadata for datasets according to DataCite standard. Core properties of DataCite standard (basics for citation/publications.) DataCite already considers DublinCore elements. "
--     * Slot: identifier Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: identifierType Description: type of identifier.
--     * Slot: creators Description: Creator(s) of the resource.
--     * Slot: title Description: Title of the resource/dataset.
--     * Slot: Publisher Description: Creator of the resource.
--     * Slot: ResourceType Description: Creator of the resource.
--     * Slot: Subject Description: Creator of the resource.
--     * Slot: Contributor Description: Creator of the resource.
--     * Slot: Date Description: Creator of the resource.
--     * Slot: Language Description: Creator of the resource.
--     * Slot: AlternateIdentifier Description: An identifier other than the primary Identifier applied to the resource being registered. This may be any alphanumeric string which is unique within its domain of issue. May be used for local identifiers, a serial number of an instrument or an inventory number. The AlternateIdentifier should be an additional identifier for the same instance of the resource (i.e., same location, same file).
--     * Slot: RelatedIdentifier Description: Identifiers of related resources. These must be globally unique identifiers.
--     * Slot: Size Description: Size (e.g., bytes, pages, inches, etc.) or duration (extent), e.g., hours, minutes, days, etc., of a resource.
--     * Slot: Format Description: Technical format of the resource.
--     * Slot: Version Description: Creator of the resource.
--     * Slot: Rights Description: Creator of the resource.
--     * Slot: Description Description: Creator of the resource.
--     * Slot: GeoLocation Description: Creator of the resource.
--     * Slot: FundingReference Description: Creator of the resource.
--     * Slot: RelatedItem Description: Creator of the resource.
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Person" Description: "A basic/standard definition of a person, which later can be further defined as scientist, beam scientist, user, etc."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Project" Description: "A research activity or initiative with defined objectives, funding, and timelines, involving one or more researchers, designed to generate data, publications, and other outputs. The project may involve multiple experiments, datasets, and contributors, and can be linked to specific funding sources and institutions."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Device" Description: "A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Sample" Description: "Core properties of a sample, discipline agnostic."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: SampleCollection_id Description: Autocreated FK slot
-- # Class: "SampleCollection" Description: "A holder for Sample objects"
--     * Slot: id Description: 
-- # Class: "Scientist" Description: "An individual involved in research activities, and their details that are important  to be referenced on experiments, projects, publivations, etc."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "CatalysisSample" Description: "Core properties of a catalysis sample."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: CatalysisSampleCollection_id Description: Autocreated FK slot
-- # Class: "Catalyst" Description: "A substance or material that increases the rate of a chemical reaction.  Class including core properties of the synthesis characterization, and other experiments. "
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "ThinFilmCatalyst" Description: "Catalyst type. Core properties of a thin film."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "PowderCatalyst" Description: "Catalyst type. Core properties of a powder catalyst."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Recipe" Description: "A detailed set of instructions outlining the materials, quantities, and procedures  required to perform a specific chemical reaction or experimental process."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Mixture" Description: "A combination of two or more substances that are mixed together,  which may retain their individual properties or interact chemically. "
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Workflow" Description: "A structured sequence of tasks, activities, or processes designed to accomplish a  specific research objective or experimental goal."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Process" Description: "A defined series of actions, steps, or operations undertaken to achieve a  specific scientific or experimental outcome (e.g. atomic layer deposition)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Experiment" Description: "A systematic investigation designed to test hypotheses, gather data, or explore  scientific principles through controlled conditions."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Measurement" Description: "Storing and describing measurements to perform on a sample."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Parameter" Description: "Associates parameters on demand to a certain experiment or measurement."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Reaction" Description: "A chemical process in which one or more substances (reactants) undergo transformation to produce new substances (products). "
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "ReactionProduct" Description: "A substance formed as a result of a chemical reaction, representing the end products  generated from the transformation of reactants."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: ReactionProductCollection_id Description: Autocreated FK slot
-- # Class: "Reactor" Description: "Equipment designed to facilitate and control chemical reactions under specified  conditions, such as temperature, pressure, and flow rates. "
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "CatalysisSampleCollection" Description: "A holder for CatalysisSample objects"
--     * Slot: id Description: 
-- # Class: "ReactionProductCollection" Description: "A holder for ReactionProduct objects"
--     * Slot: id Description: 
-- # Class: "Beamline" Description: "System within a facility designed to direct a beam of radiation toward a sample for  the purpose of analysis or experimentation."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "BeamlineExperiment" Description: "An experimental investigation conducted using a beamline."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "BeamlineScientist" Description: "An expert responsible for the operation and scientific application of beamlines  in a research facility."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "mySpot" Description: "Myspot beamline description."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "EMIL_Pink" Description: "Pink beamline description."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "EMIL_OAESE" Description: "OAESE beamline description."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "SampleEnvironment" Description: "Controlled environment in which the sample is studied (operando research)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "EnvironmentDynamics" Description: "Dynamic or time-resolved environmental conditions during an  experiment (e.g.for in-situ measurements)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "SamplePositioning" Description: "The arrangement or location of samples within an experimental setup,  critical for ensuring accurate data collection and analysis. "
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "File" Description: "Stores data related to the experiment (e.g. images, videos, or other files)."
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
CREATE TABLE "EnvironmentDynamics" (
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
CREATE TABLE "File" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataCite" (
	identifier TEXT NOT NULL, 
	"identifierType" TEXT, 
	creators TEXT NOT NULL, 
	title TEXT NOT NULL, 
	"Publisher" TEXT, 
	"ResourceType" TEXT, 
	"Subject" TEXT, 
	"Contributor" TEXT, 
	"Date" TEXT, 
	"Language" TEXT, 
	"AlternateIdentifier" TEXT, 
	"RelatedIdentifier" TEXT, 
	"Size" TEXT, 
	"Format" TEXT, 
	"Version" TEXT, 
	"Rights" TEXT, 
	"Description" TEXT, 
	"GeoLocation" TEXT, 
	"FundingReference" TEXT, 
	"RelatedItem" TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(creators) REFERENCES "Person" (id)
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