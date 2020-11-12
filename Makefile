init:
	pipenv --python 3.8
	pipenv install --dev

# Command to run everytime you make changes to verify everything works
dev: flake lint test

# Verifications to run before sending a pull request
pr: init dev


build:
	$(info Building application)
	sam build

validate:
	$(info linting SAM template)
	$(info linting CloudFormation)
	@cfn-lint template.yaml
	$(info validating SAM template)
	@sam validate

test:
	$(info running unit tests)
	tox

flake8:
	$(info running flake8 on code)
	pip install flake8
	flake8 src
	flake8 tests/unit

pylint:
	$(info running pylint on code)
	# Linter performs static analysis to catch latent bugs
	pip install pylint
	pylint src

lint: pylint flake8

clean:
	$(info cleaning project)
	# remove sam cache
	rm -rf .aws-sam

