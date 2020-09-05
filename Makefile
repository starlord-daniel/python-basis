init:
	pip install -r requirements.txt
lint:
	flake8
test:
	pytest tests --cov=app tests/
run:
	python run.py 2 3 2

.PHONY: init test