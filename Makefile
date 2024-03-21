setup:
	poetry install
	pre-commit install

format:
	ruff format --diff

lint:
	ruff check --output-format=github .

fix:
	ruff check --output-format=github . --fix
	ruff format

docker-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

run:
	python -m src.users
