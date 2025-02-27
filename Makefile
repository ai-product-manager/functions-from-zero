install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -p no:warnings -vv --cov=main --cov=calcCLI --cov=mylib test_*.py

format:	
	black *.py mylib/*.py

lint:
	pylint --disable=R,C --extension-pkg-whitelist='pydantic' main.py --ignore-patterns=test_.*?py *.py  mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 654654520205.dkr.ecr.us-east-1.amazonaws.com
	docker build -t logistics .
	docker tag logistics:latest 654654520205.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
	docker push 654654520205.dkr.ecr.us-east-1.amazonaws.com/logistics:latest
		
		
all: install lint test format deploy