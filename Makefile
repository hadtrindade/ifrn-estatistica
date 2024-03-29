clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf *egg-info
	rm -rf *tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache


install:
	pip install -e .['dev']


test:
	pytest -s tests/ -v --cov=ifrn_estatistica --cov-config=.coveragerc

isort:
	isort --recursive ifrn_estatistica

black:
	black -l 79 ifrn_estatistica