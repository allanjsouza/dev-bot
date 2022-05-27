clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .[dev] --upgrade --no-cache

install:
	pip install -e .['dev']

test:
	pytest tests/ -v

coverage:
	@ pytest tests/ -v --cov=app
	@ coverage html
	@ python scripts/coverage_report.py

release:
	@ chmod +x scripts/release.sh
	@ ./scripts/release.sh

format:
	@ isort .
	@ autopep8 --recursive --in-place --aggressive .
	@ black .
