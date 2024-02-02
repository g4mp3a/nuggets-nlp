install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora
test:
	python -m pytest -vv --cov=wikiphrases --cov=nlp --cov=main test_corenlp.py

lint:
	pylint --disable=R,C *.py nlp/*.py
	docker run --rm -i hadolint/hadolint < Dockerfile
format:
	black *.py nlp

all: install lint test format