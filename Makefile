export PYTHONPATH = mariantrans

check_dirs := mariantranslate tests

install_src:
	pip install -e .

install_src_dev:
	pip install -e .[dev]

quality:
	black --check $(check_dirs)
	isort --check-only $(check_dirs)
	flake8 $(check_dirs)

style:
	black $(check_dirs)
	isort $(check_dirs)

test:
	python -m pytest -s -vv ./tests/test.py