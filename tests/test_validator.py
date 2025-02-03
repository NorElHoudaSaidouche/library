import pytest
import json
from library.forms.validator import Validator


@pytest.fixture
def valid_data():
    with open("tests/test_validator/iphone_16_valid.json") as f:
        return json.load(f)


@pytest.fixture
def non_valid_data():
    with open("tests/test_validator/iphone_16_invalid.json") as f:
        return json.load(f)


def test_validator_valid(valid_data):
    validator = Validator()
    is_valid, message = validator.validate_data(valid_data)
    assert is_valid


def test_validator_non_valid(non_valid_data):
    validator = Validator()
    is_valid, message = validator.validate_data(non_valid_data)
    assert not is_valid
