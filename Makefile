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
	pytest tests/ -v --cov=ifrn_estatistica

