# Library

The `library` package handles defining and validating product characterization forms.

## Repository organization

The repository is organized as the following:

- **Library/forms** : the forms submodules, it contains:
    - templates: folder containing the product definition as a [jsonschema](https://json-schema.org/docs).
    - validator: A tool for validating product characterization data, ensuring it respects the defined schema.
    - docGenerator: utility for generating documentation for product characterization forms, providing easy-to-read
      outputs.
    - doc: the result of executing DocGenerator.

- **Tests:** unit tests
    - test_validator: testing two cases, one of a valid product json, and an invalid one.