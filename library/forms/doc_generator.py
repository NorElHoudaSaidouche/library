from logging import getLogger
from json_schema_for_humans.generate import generate_from_filename
from json_schema_for_humans.generation_configuration import GenerationConfiguration

logger = getLogger(__name__)


class DocGenerator:
    def __init__(self, output_file: str):
        self.jsonschema_path = "library/forms/templates/product.json"
        self.output_file = output_file

    def generate_doc(self) -> None:
        config = GenerationConfiguration(expand_buttons=True)
        generate_from_filename(self.jsonschema_path, self.output_file, config=config)
