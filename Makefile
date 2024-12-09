.PHONY: local-setup 
local-setup:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip setuptools wheel pip-tools
	.venv/bin/pip-compile --generate-hashes --output-file=requirements.txt requirements.in 
	.venv/bin/pip install -r requirements.txt

.PHONY: run-locally
run-locally:
	pytest ./tests/api/test.py


.PHONY: format 
format:
	python3 -m black ./tests/api/

.PHONY: clean 
clean:
	rm -r .venv
	find . -type d -name __pycache__ -exec rm -r {} \;

.PHONY: run 
run:
	docker compose up --build
