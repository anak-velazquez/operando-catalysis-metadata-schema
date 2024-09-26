# Auto generated from hzb_metadata_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-08-05T18:33:38
# Schema: hzb-metadata-schema
#
# id: https://w3id.org/anak-velazquez/hzb-metadata-schema
# description: (Meta)data schema HZB labs
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
CHEBI = CurieNamespace('CHEBI', 'http://example.org/UNKNOWN/CHEBI/')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://example.org/UNKNOWN/CHEMBL.COMPOUND/')
GSSO = CurieNamespace('GSSO', 'http://purl.bioontology.org/ontology/GSSO/')
MAXO = CurieNamespace('MAXO', 'http://example.org/UNKNOWN/MAXO/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://example.org/UNKNOWN/PUBCHEM.COMPOUND/')
STY = CurieNamespace('STY', 'http://example.org/UNKNOWN/STY/')
UMLSSG = CurieNamespace('UMLSSG', 'http://example.org/UNKNOWN/UMLSSG/')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://example.org/UNKNOWN/WIKIDATA/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCID = CurieNamespace('dcid', 'http://example.org/UNKNOWN/dcid/')
HZB_METADATA_SCHEMA = CurieNamespace('hzb_metadata_schema', 'https://w3id.org/anak-velazquez/hzb-metadata-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = HZB_METADATA_SCHEMA


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = HZB_METADATA_SCHEMA.ChemicalFormulaValue


# Class references
class EntityId(URIorCURIE):
    pass


class NamedThingId(EntityId):
    pass


class PersonId(NamedThingId):
    pass


class ScientistId(PersonId):
    pass


class DeviceId(NamedThingId):
    pass


class SampleId(NamedThingId):
    pass


class CatalysisSampleId(SampleId):
    pass


class ExperimentId(NamedThingId):
    pass


class BESSYId(NamedThingId):
    pass


class BeamlineId(NamedThingId):
    pass


class MyspotBeamlineId(BeamlineId):
    pass


class BeamlineExperimentId(ExperimentId):
    pass


class RockitExperimentId(BeamlineExperimentId):
    pass


class ChemicalOrDrugOrTreatment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["ChemicalOrDrugOrTreatment"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:ChemicalOrDrugOrTreatment"
    class_name: ClassVar[str] = "chemical or drug or treatment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ChemicalOrDrugOrTreatment


@dataclass
class SampleCollection(YAMLRoot):
    """
    A holder for Sample objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["SampleCollection"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:SampleCollection"
    class_name: ClassVar[str] = "SampleCollection"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SampleCollection

    entries: Optional[Union[Dict[Union[str, SampleId], Union[dict, "Sample"]], List[Union[dict, "Sample"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Sample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Organization(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["Organization"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Organization

    name: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)
        self.unknown_type = str(self.class_name)


@dataclass
class Entity(YAMLRoot):
    """
    An entity is anything that exists or has existed or will exist. Model class for all things and informational
    relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["Entity"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Entity

    id: Union[str, EntityId] = None
    iri: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.iri is not None and not isinstance(self.iri, str):
            self.iri = str(self.iri)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["NamedThing"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, str):
            self.category = str(self.category)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    A person (alive, dead, undead, or fictional).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Person

    id: Union[str, PersonId] = None
    category: str = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    gender: Optional[Union[str, "GenderEnum"]] = None
    has_employment_history: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.gender is not None and not isinstance(self.gender, GenderEnum):
            self.gender = GenderEnum(self.gender)

        if not isinstance(self.has_employment_history, list):
            self.has_employment_history = [self.has_employment_history] if self.has_employment_history is not None else []
        self.has_employment_history = [v if isinstance(v, str) else str(v) for v in self.has_employment_history]

        super().__post_init__(**kwargs)


@dataclass
class Scientist(Person):
    """
    A scientist (alive, dead, undead, or fictional).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["Scientist"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:Scientist"
    class_name: ClassVar[str] = "Scientist"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Scientist

    id: Union[str, ScientistId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientistId):
            self.id = ScientistId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Device(NamedThing):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["Device"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:Device"
    class_name: ClassVar[str] = "device"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Device

    id: Union[str, DeviceId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Sample(NamedThing):
    """
    Represents a Sample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["Sample"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Sample

    id: Union[str, SampleId] = None
    category: str = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass
class CatalysisSample(Sample):
    """
    core parameters of a catalysis sample #metadata terms (parameters) are mapped to nfdi voc4cat
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["CatalysisSample"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:CatalysisSample"
    class_name: ClassVar[str] = "CatalysisSample"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CatalysisSample

    id: Union[str, CatalysisSampleId] = None
    category: str = None
    sample_environment: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalysisSampleId):
            self.id = CatalysisSampleId(self.id)

        if self.sample_environment is not None and not isinstance(self.sample_environment, str):
            self.sample_environment = str(self.sample_environment)

        super().__post_init__(**kwargs)


@dataclass
class Experiment(NamedThing):
    """
    something following a protocol?
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["Experiment"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:Experiment"
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Experiment

    id: Union[str, ExperimentId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentId):
            self.id = ExperimentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BESSY(NamedThing):
    """
    Sonal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["BESSY"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:BESSY"
    class_name: ClassVar[str] = "BESSY"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.BESSY

    id: Union[str, BESSYId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BESSYId):
            self.id = BESSYId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Beamline(NamedThing):
    """
    Sonal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["Beamline"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:Beamline"
    class_name: ClassVar[str] = "Beamline"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Beamline

    id: Union[str, BeamlineId] = None
    category: str = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamlineId):
            self.id = BeamlineId(self.id)

        self.type = str(self.class_name)

        super().__post_init__(**kwargs)
        self.unknown_type = str(self.class_name)


    def __new__(cls, *args, **kwargs):

        type_designator = "type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass
class MyspotBeamline(Beamline):
    """
    Sonal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["MyspotBeamline"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:MyspotBeamline"
    class_name: ClassVar[str] = "Myspot_Beamline"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.MyspotBeamline

    id: Union[str, MyspotBeamlineId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MyspotBeamlineId):
            self.id = MyspotBeamlineId(self.id)

        super().__post_init__(**kwargs)
        self.unknown_type = str(self.class_name)


@dataclass
class BeamlineExperiment(Experiment):
    """
    Sonal
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["BeamlineExperiment"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:BeamlineExperiment"
    class_name: ClassVar[str] = "BeamlineExperiment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.BeamlineExperiment

    id: Union[str, BeamlineExperimentId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamlineExperimentId):
            self.id = BeamlineExperimentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class RockitExperiment(BeamlineExperiment):
    """
    describing the standard setup for ROCK-IT beamline experiment. Sonal + Ana
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["RockitExperiment"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:RockitExperiment"
    class_name: ClassVar[str] = "Rockit_experiment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.RockitExperiment

    id: Union[str, RockitExperimentId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RockitExperimentId):
            self.id = RockitExperimentId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

class GenderEnum(EnumDefinitionImpl):

    Woman = PermissibleValue(
        text="Woman",
        description="identified as woman",
        meaning=GSSO["000369"])
    Masculine = PermissibleValue(
        text="Masculine",
        description="masculine")
    Diverse = PermissibleValue(
        text="Diverse",
        description="other")

    _defn = EnumDefinition(
        name="GenderEnum",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=HZB_METADATA_SCHEMA.id, domain=None, range=URIRef)

slots.iri = Slot(uri=HZB_METADATA_SCHEMA.iri, name="iri", curie=HZB_METADATA_SCHEMA.curie('iri'),
                   model_uri=HZB_METADATA_SCHEMA.iri, domain=None, range=Optional[str])

slots.category = Slot(uri=HZB_METADATA_SCHEMA.category, name="category", curie=HZB_METADATA_SCHEMA.curie('category'),
                   model_uri=HZB_METADATA_SCHEMA.category, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=HZB_METADATA_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=HZB_METADATA_SCHEMA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=HZB_METADATA_SCHEMA.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=HZB_METADATA_SCHEMA.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=HZB_METADATA_SCHEMA.age_in_years, name="age_in_years", curie=HZB_METADATA_SCHEMA.curie('age_in_years'),
                   model_uri=HZB_METADATA_SCHEMA.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=HZB_METADATA_SCHEMA.vital_status, name="vital_status", curie=HZB_METADATA_SCHEMA.curie('vital_status'),
                   model_uri=HZB_METADATA_SCHEMA.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.gender = Slot(uri=SCHEMA.gender, name="gender", curie=SCHEMA.curie('gender'),
                   model_uri=HZB_METADATA_SCHEMA.gender, domain=None, range=Optional[Union[str, "GenderEnum"]])

slots.has_employment_history = Slot(uri=HZB_METADATA_SCHEMA.has_employment_history, name="has_employment_history", curie=HZB_METADATA_SCHEMA.curie('has_employment_history'),
                   model_uri=HZB_METADATA_SCHEMA.has_employment_history, domain=None, range=Optional[Union[str, List[str]]])

slots.current_address = Slot(uri=HZB_METADATA_SCHEMA.current_address, name="current_address", curie=HZB_METADATA_SCHEMA.curie('current_address'),
                   model_uri=HZB_METADATA_SCHEMA.current_address, domain=None, range=Optional[str])

slots.catalysisSample__sample_environment = Slot(uri=HZB_METADATA_SCHEMA.sample_environment, name="catalysisSample__sample_environment", curie=HZB_METADATA_SCHEMA.curie('sample_environment'),
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__sample_environment, domain=None, range=Optional[str])

slots.sampleCollection__entries = Slot(uri=HZB_METADATA_SCHEMA.entries, name="sampleCollection__entries", curie=HZB_METADATA_SCHEMA.curie('entries'),
                   model_uri=HZB_METADATA_SCHEMA.sampleCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]])

slots.beamline__type = Slot(uri=HZB_METADATA_SCHEMA.type, name="beamline__type", curie=HZB_METADATA_SCHEMA.curie('type'),
                   model_uri=HZB_METADATA_SCHEMA.beamline__type, domain=None, range=Optional[str])

slots.organization__name = Slot(uri=HZB_METADATA_SCHEMA.name, name="organization__name", curie=HZB_METADATA_SCHEMA.curie('name'),
                   model_uri=HZB_METADATA_SCHEMA.organization__name, domain=None, range=Optional[str])

slots.organization__type = Slot(uri=HZB_METADATA_SCHEMA.type, name="organization__type", curie=HZB_METADATA_SCHEMA.curie('type'),
                   model_uri=HZB_METADATA_SCHEMA.organization__type, domain=None, range=Optional[str])

slots.Sample_primary_email = Slot(uri=SCHEMA.email, name="Sample_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=HZB_METADATA_SCHEMA.Sample_primary_email, domain=Sample, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.NamedThing_category = Slot(uri=HZB_METADATA_SCHEMA.category, name="NamedThing_category", curie=HZB_METADATA_SCHEMA.curie('category'),
                   model_uri=HZB_METADATA_SCHEMA.NamedThing_category, domain=NamedThing, range=str)