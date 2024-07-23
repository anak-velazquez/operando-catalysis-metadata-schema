# hzb-metadata-schema

(Meta)data schema HZB labs

## Website

[https://anak-velazquez.github.io/hzb-metadata-schema](https://anak-velazquez.github.io/hzb-metadata-schema)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
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
