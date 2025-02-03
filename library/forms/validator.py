from jsonschema import ValidationError, validate
from library.utils import read_json_from_file


class Validator:
    def __init__(self):
        self.jsonschema = read_json_from_file("library/forms/templates/product.json")

    def validate_data(self, data: dict) -> tuple[bool, str]:
        try:
            validate(instance=data, schema=self.jsonschema)
            return True, "The Data is valid"
        except ValidationError as e:
            return False, f"The Data is invalid. Error: {e.message}"
