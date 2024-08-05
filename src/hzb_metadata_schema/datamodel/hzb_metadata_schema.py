# Auto generated from hzb_metadata_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-08-05T15:01:15
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
BFO = CurieNamespace('BFO', 'http://example.org/UNKNOWN/BFO/')
CHEBI = CurieNamespace('CHEBI', 'http://example.org/UNKNOWN/CHEBI/')
CHEMBL_COMPOUND = CurieNamespace('CHEMBL_COMPOUND', 'http://example.org/UNKNOWN/CHEMBL.COMPOUND/')
MAXO = CurieNamespace('MAXO', 'http://example.org/UNKNOWN/MAXO/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PUBCHEM_COMPOUND = CurieNamespace('PUBCHEM_COMPOUND', 'http://example.org/UNKNOWN/PUBCHEM.COMPOUND/')
STY = CurieNamespace('STY', 'http://example.org/UNKNOWN/STY/')
UMLSSG = CurieNamespace('UMLSSG', 'http://example.org/UNKNOWN/UMLSSG/')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://example.org/UNKNOWN/WIKIDATA/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCID = CurieNamespace('dcid', 'http://example.org/UNKNOWN/dcid/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
HZB_METADATA_SCHEMA = CurieNamespace('hzb_metadata_schema', 'https://w3id.org/anak-velazquez/hzb-metadata-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
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
    class_name: ClassVar[str] = "sampleCollection"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SampleCollection

    entries: Optional[Union[Union[dict, "Sample"], List[Union[dict, "Sample"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Sample, key_name="category", keyed=False)

        super().__post_init__(**kwargs)


class Entity(YAMLRoot):
    """
    Root Biolink Model class for all things and informational relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["Entity"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:Entity"
    class_name: ClassVar[str] = "entity"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Entity


@dataclass
class NamedThing(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["NamedThing"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:NamedThing"
    class_name: ClassVar[str] = "namedThing"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.NamedThing

    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, str):
            self.category = str(self.category)

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

    category: str = None

@dataclass
class Sample(NamedThing):
    """
    Represents a Sample
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["Sample"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:Sample"
    class_name: ClassVar[str] = "sample"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Sample

    category: str = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
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
    class_name: ClassVar[str] = "catalysisSample"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CatalysisSample

    category: str = None
    sample_environment: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.sample_environment is not None and not isinstance(self.sample_environment, str):
            self.sample_environment = str(self.sample_environment)

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

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=HZB_METADATA_SCHEMA.id, domain=None, range=URIRef)

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

slots.catalysisSample__sample_environment = Slot(uri=HZB_METADATA_SCHEMA.sample_environment, name="catalysisSample__sample_environment", curie=HZB_METADATA_SCHEMA.curie('sample_environment'),
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__sample_environment, domain=None, range=Optional[str])

slots.sampleCollection__entries = Slot(uri=HZB_METADATA_SCHEMA.entries, name="sampleCollection__entries", curie=HZB_METADATA_SCHEMA.curie('entries'),
                   model_uri=HZB_METADATA_SCHEMA.sampleCollection__entries, domain=None, range=Optional[Union[Union[dict, Sample], List[Union[dict, Sample]]]])

slots.category = Slot(uri=HZB_METADATA_SCHEMA.category, name="category", curie=HZB_METADATA_SCHEMA.curie('category'),
                   model_uri=HZB_METADATA_SCHEMA.category, domain=None, range=str)

slots.sample_primary_email = Slot(uri=SCHEMA.email, name="sample_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=HZB_METADATA_SCHEMA.sample_primary_email, domain=Sample, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.namedThing_category = Slot(uri=HZB_METADATA_SCHEMA.category, name="namedThing_category", curie=HZB_METADATA_SCHEMA.curie('category'),
                   model_uri=HZB_METADATA_SCHEMA.namedThing_category, domain=NamedThing, range=str)