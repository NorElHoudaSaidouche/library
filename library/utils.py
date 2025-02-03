import json


def read_json_from_file(file_path: str) -> dict:
    """Read JSON data from a file, ensuring a dictionary is returned."""
    try:
        with open(file_path) as f:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, TypeError):
        return {}
