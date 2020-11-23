# Command to run everytime you make changes to verify everything works
dev: lint validate build

build:
	$(info Building application)
	sam build

validate:
	$(info linting SAM template)
	$(info linting CloudFormation)
	@cfn-lint template.yaml
	$(info validating SAM template)
	@sam validate

lint: flake8 isort black

flake8:
	$(info running flake8)
	flake8 src
	flake8 tests

isort:
	$(info sorting imports with isort)
	isort src
	isort tests

black:
	$(info formatting with black)
	black -l 120 src
	black -l 120 tests

test:
	$(info running unit tests)
	tox

clean:
	$(info cleaning project)
	# remove output from other stages
	rm -rf .aws-sam
	rm -rf .eggs
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .tox
