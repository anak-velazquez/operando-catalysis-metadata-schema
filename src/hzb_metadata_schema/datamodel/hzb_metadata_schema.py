# Auto generated from hzb_metadata_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-09-30T17:56:39
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
GSSO = CurieNamespace('GSSO', 'http://purl.bioontology.org/ontology/GSSO/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
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


class NamedEntityId(EntityId):
    pass


class DataCiteId(NamedEntityId):
    pass


class PersonId(NamedEntityId):
    pass


class ProjectId(NamedEntityId):
    pass


class DeviceId(NamedEntityId):
    pass


class SampleId(NamedEntityId):
    pass


class ScientistId(PersonId):
    pass


class CatalysisSampleId(SampleId):
    pass


class CatalystId(CatalysisSampleId):
    pass


class ThinFilmCatalystId(CatalystId):
    pass


class PowderCatalystId(CatalystId):
    pass


class RecipeId(NamedEntityId):
    pass


class MixtureId(NamedEntityId):
    pass


class WorkflowId(NamedEntityId):
    pass


class ProcessId(NamedEntityId):
    pass


class ExperimentId(NamedEntityId):
    pass


class MeasurementId(NamedEntityId):
    pass


class ParameterId(NamedEntityId):
    pass


class ReactionId(NamedEntityId):
    pass


class ReactionProductId(NamedEntityId):
    pass


class ReactorId(NamedEntityId):
    pass


class BeamlineId(NamedEntityId):
    pass


class BeamlineExperimentId(ExperimentId):
    pass


class BeamlineScientistId(PersonId):
    pass


class MySpotId(BeamlineId):
    pass


class EMILPinkId(BeamlineId):
    pass


class EMILOAESEId(BeamlineId):
    pass


class SampleEnvironmentId(NamedEntityId):
    pass


class EnvironmentDynamicsId(NamedEntityId):
    pass


class SamplePositioningId(NamedEntityId):
    pass


class FileId(NamedEntityId):
    pass


class ChemicalOrDrugOrTreatment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["ChemicalOrDrugOrTreatment"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:ChemicalOrDrugOrTreatment"
    class_name: ClassVar[str] = "chemical or drug or treatment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ChemicalOrDrugOrTreatment


@dataclass
class Entity(YAMLRoot):
    """
    An entity is anything that exists or has existed or will exist. Model class for all things and informational
    relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/Entity")
    class_class_curie: ClassVar[str] = None
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
class NamedEntity(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/NamedEntity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.NamedEntity

    id: Union[str, NamedEntityId] = None
    category: str = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self._is_empty(self.category):
            self.MissingRequiredField("category")
        if not isinstance(self.category, str):
            self.category = str(self.category)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass
class DataCite(NamedEntity):
    """
    Represents metadata for datasets according to DataCite standard. Core properties of DataCite standard (basics for
    citation/publications.) DataCite already considers DublinCore elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/DataCite")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataCite"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.DataCite

    id: Union[str, DataCiteId] = None
    category: str = None
    identifier: str = None
    creators: Union[str, PersonId] = None
    title: str = None
    identifierType: Optional[str] = None
    Publisher: Optional[str] = None
    ResourceType: Optional[str] = None
    Subject: Optional[str] = None
    Contributor: Optional[str] = None
    Date: Optional[str] = None
    Language: Optional[str] = None
    AlternateIdentifier: Optional[str] = None
    RelatedIdentifier: Optional[str] = None
    Size: Optional[str] = None
    Format: Optional[str] = None
    Version: Optional[str] = None
    Rights: Optional[str] = None
    Description: Optional[str] = None
    GeoLocation: Optional[str] = None
    FundingReference: Optional[str] = None
    RelatedItem: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataCiteId):
            self.id = DataCiteId(self.id)

        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self._is_empty(self.creators):
            self.MissingRequiredField("creators")
        if not isinstance(self.creators, PersonId):
            self.creators = PersonId(self.creators)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.identifierType is not None and not isinstance(self.identifierType, str):
            self.identifierType = str(self.identifierType)

        if self.Publisher is not None and not isinstance(self.Publisher, str):
            self.Publisher = str(self.Publisher)

        if self.ResourceType is not None and not isinstance(self.ResourceType, str):
            self.ResourceType = str(self.ResourceType)

        if self.Subject is not None and not isinstance(self.Subject, str):
            self.Subject = str(self.Subject)

        if self.Contributor is not None and not isinstance(self.Contributor, str):
            self.Contributor = str(self.Contributor)

        if self.Date is not None and not isinstance(self.Date, str):
            self.Date = str(self.Date)

        if self.Language is not None and not isinstance(self.Language, str):
            self.Language = str(self.Language)

        if self.AlternateIdentifier is not None and not isinstance(self.AlternateIdentifier, str):
            self.AlternateIdentifier = str(self.AlternateIdentifier)

        if self.RelatedIdentifier is not None and not isinstance(self.RelatedIdentifier, str):
            self.RelatedIdentifier = str(self.RelatedIdentifier)

        if self.Size is not None and not isinstance(self.Size, str):
            self.Size = str(self.Size)

        if self.Format is not None and not isinstance(self.Format, str):
            self.Format = str(self.Format)

        if self.Version is not None and not isinstance(self.Version, str):
            self.Version = str(self.Version)

        if self.Rights is not None and not isinstance(self.Rights, str):
            self.Rights = str(self.Rights)

        if self.Description is not None and not isinstance(self.Description, str):
            self.Description = str(self.Description)

        if self.GeoLocation is not None and not isinstance(self.GeoLocation, str):
            self.GeoLocation = str(self.GeoLocation)

        if self.FundingReference is not None and not isinstance(self.FundingReference, str):
            self.FundingReference = str(self.FundingReference)

        if self.RelatedItem is not None and not isinstance(self.RelatedItem, str):
            self.RelatedItem = str(self.RelatedItem)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedEntity):
    """
    A basic/standard definition of a person, which later can be further defined as scientist, beam scientist, user,
    etc.
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
class Project(NamedEntity):
    """
    A research activity or initiative with defined objectives, funding, and timelines, involving one or more
    researchers, designed to generate data, publications, and other outputs. The project may involve multiple
    experiments, datasets, and contributors, and can be linked to specific funding sources and institutions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/Project")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Project

    id: Union[str, ProjectId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Device(NamedEntity):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/Device")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Device"
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
class Sample(NamedEntity):
    """
    Core properties of a sample, discipline agnostic.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/Sample")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Sample

    id: Union[str, SampleId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SampleCollection(YAMLRoot):
    """
    A holder for Sample objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/SampleCollection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SampleCollection"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SampleCollection

    entries: Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Sample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Scientist(Person):
    """
    An individual involved in research activities, and their details that are important to be referenced on
    experiments, projects, publivations, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Scientist")
    class_class_curie: ClassVar[str] = None
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
class CatalysisSample(Sample):
    """
    Core properties of a catalysis sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CatalysisSample")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CatalysisSample"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CatalysisSample

    id: Union[str, CatalysisSampleId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalysisSampleId):
            self.id = CatalysisSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Catalyst(CatalysisSample):
    """
    A substance or material that increases the rate of a chemical reaction. Class including core properties of the
    synthesis characterization, and other experiments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Catalyst")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Catalyst"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Catalyst

    id: Union[str, CatalystId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalystId):
            self.id = CatalystId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ThinFilmCatalyst(Catalyst):
    """
    Catalyst type. Core properties of a thin film.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/ThinFilmCatalyst")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ThinFilmCatalyst"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ThinFilmCatalyst

    id: Union[str, ThinFilmCatalystId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThinFilmCatalystId):
            self.id = ThinFilmCatalystId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PowderCatalyst(Catalyst):
    """
    Catalyst type. Core properties of a powder catalyst.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/PowderCatalyst")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PowderCatalyst"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.PowderCatalyst

    id: Union[str, PowderCatalystId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PowderCatalystId):
            self.id = PowderCatalystId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Recipe(NamedEntity):
    """
    A detailed set of instructions outlining the materials, quantities, and procedures required to perform a specific
    chemical reaction or experimental process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Recipe")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Recipe"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Recipe

    id: Union[str, RecipeId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecipeId):
            self.id = RecipeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Mixture(NamedEntity):
    """
    A combination of two or more substances that are mixed together, which may retain their individual properties or
    interact chemically.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Mixture")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Mixture"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Mixture

    id: Union[str, MixtureId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MixtureId):
            self.id = MixtureId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Workflow(NamedEntity):
    """
    A structured sequence of tasks, activities, or processes designed to accomplish a specific research objective or
    experimental goal.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Workflow")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Workflow"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Workflow

    id: Union[str, WorkflowId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkflowId):
            self.id = WorkflowId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Process(NamedEntity):
    """
    A defined series of actions, steps, or operations undertaken to achieve a specific scientific or experimental
    outcome (e.g. atomic layer deposition).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Process")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Process

    id: Union[str, ProcessId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessId):
            self.id = ProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Experiment(NamedEntity):
    """
    A systematic investigation designed to test hypotheses, gather data, or explore scientific principles through
    controlled conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Experiment")
    class_class_curie: ClassVar[str] = None
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
class Measurement(NamedEntity):
    """
    Storing and describing measurements to perform on a sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Measurement")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Measurement

    id: Union[str, MeasurementId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeasurementId):
            self.id = MeasurementId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Parameter(NamedEntity):
    """
    Associates parameters on demand to a certain experiment or measurement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Parameter")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Parameter

    id: Union[str, ParameterId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParameterId):
            self.id = ParameterId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Reaction(NamedEntity):
    """
    A chemical process in which one or more substances (reactants) undergo transformation to produce new substances
    (products).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Reaction")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Reaction"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Reaction

    id: Union[str, ReactionId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionId):
            self.id = ReactionId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class ReactionProduct(NamedEntity):
    """
    A substance formed as a result of a chemical reaction, representing the end products generated from the
    transformation of reactants.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/ReactionProduct")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ReactionProduct"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ReactionProduct

    id: Union[str, ReactionProductId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionProductId):
            self.id = ReactionProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Reactor(NamedEntity):
    """
    Equipment designed to facilitate and control chemical reactions under specified conditions, such as temperature,
    pressure, and flow rates.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Reactor")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Reactor"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Reactor

    id: Union[str, ReactorId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactorId):
            self.id = ReactorId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CatalysisSampleCollection(YAMLRoot):
    """
    A holder for CatalysisSample objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CatalysisSampleCollection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CatalysisSampleCollection"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CatalysisSampleCollection

    entries: Optional[Union[Dict[Union[str, CatalysisSampleId], Union[dict, CatalysisSample]], List[Union[dict, CatalysisSample]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=CatalysisSample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class ReactionProductCollection(YAMLRoot):
    """
    A holder for ReactionProduct objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/ReactionProductCollection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ReactionProductCollection"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ReactionProductCollection

    entries: Optional[Union[Dict[Union[str, ReactionProductId], Union[dict, ReactionProduct]], List[Union[dict, ReactionProduct]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=ReactionProduct, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Beamline(NamedEntity):
    """
    System within a facility designed to direct a beam of radiation toward a sample for the purpose of analysis or
    experimentation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/Beamline")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Beamline"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Beamline

    id: Union[str, BeamlineId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamlineId):
            self.id = BeamlineId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class BeamlineExperiment(Experiment):
    """
    An experimental investigation conducted using a beamline.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/BeamlineExperiment")
    class_class_curie: ClassVar[str] = None
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
class BeamlineScientist(Person):
    """
    An expert responsible for the operation and scientific application of beamlines  in a research facility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/BeamlineScientist")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BeamlineScientist"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.BeamlineScientist

    id: Union[str, BeamlineScientistId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamlineScientistId):
            self.id = BeamlineScientistId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MySpot(Beamline):
    """
    Myspot beamline description.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/MySpot")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "mySpot"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.MySpot

    id: Union[str, MySpotId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MySpotId):
            self.id = MySpotId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EMILPink(Beamline):
    """
    Pink beamline description.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/EMILPink")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EMIL_Pink"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.EMILPink

    id: Union[str, EMILPinkId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EMILPinkId):
            self.id = EMILPinkId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EMILOAESE(Beamline):
    """
    OAESE beamline description.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/EMILOAESE")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EMIL_OAESE"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.EMILOAESE

    id: Union[str, EMILOAESEId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EMILOAESEId):
            self.id = EMILOAESEId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SampleEnvironment(NamedEntity):
    """
    Controlled environment in which the sample is studied (operando research).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/operandoCatalysis/SampleEnvironment")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SampleEnvironment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SampleEnvironment

    id: Union[str, SampleEnvironmentId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleEnvironmentId):
            self.id = SampleEnvironmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class EnvironmentDynamics(NamedEntity):
    """
    Dynamic or time-resolved environmental conditions during an  experiment (e.g.for in-situ measurements).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/operandoCatalysis/EnvironmentDynamics")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EnvironmentDynamics"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.EnvironmentDynamics

    id: Union[str, EnvironmentDynamicsId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentDynamicsId):
            self.id = EnvironmentDynamicsId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SamplePositioning(NamedEntity):
    """
    The arrangement or location of samples within an experimental setup, critical for ensuring accurate data
    collection and analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/operandoCatalysis/SamplePositioning")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SamplePositioning"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SamplePositioning

    id: Union[str, SamplePositioningId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamplePositioningId):
            self.id = SamplePositioningId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class File(NamedEntity):
    """
    Stores data related to the experiment (e.g. images, videos, or other files).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/operandoCatalysis/File")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.File

    id: Union[str, FileId] = None
    category: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileId):
            self.id = FileId(self.id)

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

slots.iri = Slot(uri="str(uriorcurie)", name="iri", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.iri, domain=None, range=Optional[str])

slots.category = Slot(uri="str(uriorcurie)", name="category", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.category, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=HZB_METADATA_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=HZB_METADATA_SCHEMA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=HZB_METADATA_SCHEMA.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=HZB_METADATA_SCHEMA.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri="str(uriorcurie)", name="age_in_years", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri="str(uriorcurie)", name="vital_status", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.gender = Slot(uri=SCHEMA.gender, name="gender", curie=SCHEMA.curie('gender'),
                   model_uri=HZB_METADATA_SCHEMA.gender, domain=None, range=Optional[Union[str, "GenderEnum"]])

slots.has_employment_history = Slot(uri="str(uriorcurie)", name="has_employment_history", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.has_employment_history, domain=None, range=Optional[Union[str, List[str]]])

slots.current_address = Slot(uri="str(uriorcurie)", name="current_address", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.current_address, domain=None, range=Optional[str])

slots.dataCite__identifier = Slot(uri="str(uriorcurie)", name="dataCite__identifier", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__identifier, domain=None, range=str)

slots.dataCite__identifierType = Slot(uri="str(uriorcurie)", name="dataCite__identifierType", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__identifierType, domain=None, range=Optional[str])

slots.dataCite__creators = Slot(uri="str(uriorcurie)", name="dataCite__creators", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__creators, domain=None, range=Union[str, PersonId])

slots.dataCite__title = Slot(uri="str(uriorcurie)", name="dataCite__title", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__title, domain=None, range=str)

slots.dataCite__Publisher = Slot(uri="str(uriorcurie)", name="dataCite__Publisher", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Publisher, domain=None, range=Optional[str])

slots.dataCite__ResourceType = Slot(uri="str(uriorcurie)", name="dataCite__ResourceType", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__ResourceType, domain=None, range=Optional[str])

slots.dataCite__Subject = Slot(uri="str(uriorcurie)", name="dataCite__Subject", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Subject, domain=None, range=Optional[str])

slots.dataCite__Contributor = Slot(uri="str(uriorcurie)", name="dataCite__Contributor", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Contributor, domain=None, range=Optional[str])

slots.dataCite__Date = Slot(uri="str(uriorcurie)", name="dataCite__Date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Date, domain=None, range=Optional[str])

slots.dataCite__Language = Slot(uri="str(uriorcurie)", name="dataCite__Language", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Language, domain=None, range=Optional[str])

slots.dataCite__AlternateIdentifier = Slot(uri="str(uriorcurie)", name="dataCite__AlternateIdentifier", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__AlternateIdentifier, domain=None, range=Optional[str])

slots.dataCite__RelatedIdentifier = Slot(uri="str(uriorcurie)", name="dataCite__RelatedIdentifier", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__RelatedIdentifier, domain=None, range=Optional[str])

slots.dataCite__Size = Slot(uri="str(uriorcurie)", name="dataCite__Size", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Size, domain=None, range=Optional[str])

slots.dataCite__Format = Slot(uri="str(uriorcurie)", name="dataCite__Format", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Format, domain=None, range=Optional[str])

slots.dataCite__Version = Slot(uri="str(uriorcurie)", name="dataCite__Version", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Version, domain=None, range=Optional[str])

slots.dataCite__Rights = Slot(uri="str(uriorcurie)", name="dataCite__Rights", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Rights, domain=None, range=Optional[str])

slots.dataCite__Description = Slot(uri="str(uriorcurie)", name="dataCite__Description", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Description, domain=None, range=Optional[str])

slots.dataCite__GeoLocation = Slot(uri="str(uriorcurie)", name="dataCite__GeoLocation", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__GeoLocation, domain=None, range=Optional[str])

slots.dataCite__FundingReference = Slot(uri="str(uriorcurie)", name="dataCite__FundingReference", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__FundingReference, domain=None, range=Optional[str])

slots.dataCite__RelatedItem = Slot(uri="str(uriorcurie)", name="dataCite__RelatedItem", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__RelatedItem, domain=None, range=Optional[str])

slots.sampleCollection__entries = Slot(uri="str(uriorcurie)", name="sampleCollection__entries", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sampleCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]])

slots.catalysisSampleCollection__entries = Slot(uri="str(uriorcurie)", name="catalysisSampleCollection__entries", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSampleCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, CatalysisSampleId], Union[dict, CatalysisSample]], List[Union[dict, CatalysisSample]]]])

slots.reactionProductCollection__entries = Slot(uri="str(uriorcurie)", name="reactionProductCollection__entries", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.reactionProductCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ReactionProductId], Union[dict, ReactionProduct]], List[Union[dict, ReactionProduct]]]])

slots.NamedEntity_category = Slot(uri="str(uriorcurie)", name="NamedEntity_category", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.NamedEntity_category, domain=NamedEntity, range=str)