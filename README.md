# hzb-metadata-schema

(Meta)data schema HZB labs. A datamodel for describing entities and their semantic associations (vocabularies/ontologies) for scientific (particularly catalytic) data at HZB.
At the moment, this schema is organized into 2 separate modules:
* energy definitions
* matter definitions 

# Basic content for our yml schema definitions:
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
  
# Mappings to: 
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

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
