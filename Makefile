init:
	pip install "poetry==1.8"
	poetry install --all-extras --quiet
	poetry run pre-commit install

style:
	git diff --name-only main | SKIP=no-commit-to-branch poetry run xargs pre-commit run --files

test:
	poetry run pytest -vs tests/
