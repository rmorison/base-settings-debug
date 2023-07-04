.PHONY: test pre-commit

test:
	poetry run pytest finex_engine --cov=finex_engine --cov-report=term --cov-report=html

pre-commit:
	poetry run pre-commit run --all-files
