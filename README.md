pre-commit-chatgpt-config
=========================

A pre-commit hook that submits changed file to chatgpt to get it check out the change.

Make sure requirement python modules are installed:

	pip install -r requirements.txt

Then install the pre-commit hook in any git you want to use it in by moving `.pre-commit-config.yaml` and the `./scripts` directory to that chosen git & running `pre-commit install`.
