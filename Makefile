.PHONY: install shell format lint test sec export configs

install:
	@poetry install

shell:
	@poetry shell

format:
	@isort .
	@blue .

lint:
	@blue . --check
	@isort . --check
	@prospector --no-autodetect

test:
	@pytest -s -m 'not api'

sec:
	@safety check

export:
	@poetry export -f requirements.txt --output requirements.txt

configs:
	dynaconf -i src.config.settings list
