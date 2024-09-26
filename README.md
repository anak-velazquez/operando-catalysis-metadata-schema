# hzb-metadata-schema

(Meta)data schema HZB labs. A datamodel for describing entities and their semantic associations (vocabularies/ontologies) for scientific (particularly catalytic) data at HZB.

At the moment, this schema is organized into 2 separate modules:
* energy definitions
* matter definitions 

Mappings to: 
* voc4cat
* Chemical Entities Mixtures and Reactions Ontological Framework
* NeXus definitions?? -

## Website

[https://anak-velazquez.github.io/hzb-metadata-schema](https://anak-velazquez.github.io/hzb-metadata-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these in develop branch)
  * [hzb_metadata_schema](src/hzb_metadata_schema)
    * [schema](src/hzb_metadata_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/hzb_metadata_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>


### Basic content for our yml schema definitions:
* names, identifiers, and metadata
  * id – the unique identifier for the schema, as a IRI
  * name – the schema name. Use only alphanumeric characters, underscores, and dashes
  * description – a summary of the schema. Can include markdown formatting
  * license – CC0 recommended (I put MIT just to have something now, has to be changed)
* modules
  * imports – allows for modular development. See imports
* prefix management
  * prefixes – A map of prefixes. See prefixes
  * default_prefixes – The prefix used for all elements in this schema
  * default_curi_maps – prefix maps from prefixcommons
* other
  * default_range – The default range for all slots

See also uris-and-mappings: https://linkml.io/linkml/schemas/models.html 
  
### Conventions
ATM following the same conventions a Biolink. In Biolink Model YAML any class, slot, or type is defined in `sentence case`  form. When this model is compiled to various forms (like JSON-Schema, OWL, Markdown) the representation is based on the following convention:

- classes are named in `CamelCase`  form
- slots are named in `snake_case` form
- types are named in `snake_case` form

At a glance the structure is as follows,
- Classes

  - Entities
  - Associations
  - Mixins
- Slots
  - Predicates
  - Node Properties
  - Edge Properties
- Types

A `class` represents an entity or an association. A class can have one more `slots` (properties). Within the Biolink Model there are two hierarchies of classes: `Named Things` and `Associations`; Named Things are disjoint from Associations. They do share a common ancestor class: `entity`.

`Named Things`: classes that represent real world entities such as genes, diseases, chemical substances, etc. In a graph serialization, 'Named Things' are represented by nodes in a graph. Each class in the named thing has one or more slots (properties). The root of the "Named Things" hierarchy is the biolink:NamedThing class.

`Associations`: classes that represent an assertion or statement. In RDF sense, an association is an `rdf:Statement`. In a graph formalism, associations are represented using edges in a graph. In general, Associations have three main properties (or slots): subject: the subject of the association; predicate: the predicate or relationship between the subject and the object of the association; object: the object of the association These three properties (or slots) define what Biolink calls a "core triple".

A `slot` is similar to `rdf:Property` where it can link: i) an instance of a class to another instance of a class; ii) an instance of a class to a literal/data type. slot_usage slot can be used to specify how a particular slot ought to be used in a class.

The `mixin:true` setting is used to extend the properties (or slots) of a class, without changing its position in the class hierarchy. Mixins can be extremely helpful in a number of ways: 1) to generalize a set of attributes that can apply to classes in different parts of the class hierarchy, 2) reduce duplication of shared attributes between classes that do not inherit from one another.

The `aliases` slot can be used to define a list of aliases for a Model class (or slot). This is useful for adding synonymous names to your class (or slot).


The `slot_uri` slot can be used to define a canonical URI that is the true representation for that particular slot. That is, the value of slot_uri can be used interchangeably with the slot being defined.

`id_prefixes` slot can be used to define a list of valid ID prefixes that instances of this class ought to have as part of their CURIE. The order of the list matters since its a prioritized list with the ID prefix with the highest priority appearing at the top of the list.

Please check more details here: https://github.com/biolink/biolink-model/blob/master/src/docs/understanding-the-model.md 


## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
