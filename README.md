# MLOps Lab 1 – Calculator with Testing and CI

![Pytest](https://github.com/piyush1420/mlops-lab1/actions/workflows/pytest_action.yml/badge.svg)
![Unittests](https://github.com/piyush1420/mlops-lab1/actions/workflows/unittest_action.yml/badge.svg)

Lab 1 for IE-7374 MLOps, based on `Github_Labs/Lab1` from the course repo.
It covers a virtual environment, a structured repo, unit tests with pytest
and unittest, and GitHub Actions workflows that run the tests on every push.

## Project structure

```
.github/workflows/
    pytest_action.yml      runs pytest and uploads a test report
    unittest_action.yml    runs the unittest suite
data/                      placeholder for datasets
src/calculator.py          calculator functions
test/test_pytest.py        pytest tests
test/test_unittest.py      unittest tests
requirements.txt
```

## What I changed from the original lab

### calculator.py
- Input checking moved into one helper function, `check_numbers`, instead of repeating the same check in every function.
- `True` and `False` are now rejected. Python treats them as numbers, so the original accepted `fun1(True, 2)` and returned 3.
- `fun4(x, y)` now returns the sum of `fun1`, `fun2` and `fun3`, and checks its inputs (the original `fun4` added three numbers with no checks).
- New functions: `fun6` (power), `fun7` (average of a list), `fun8` (square root), each with its own error checks.

### Tests
- Added pytest and unittest tests for `fun6`, `fun7`, `fun8` and for rejecting `True`/`False`.
- Added `fun5` tests to the unittest file (the original only tested `fun1` to `fun4`).
- Added error tests using `pytest.raises` and `assertRaises`.

### GitHub Actions
- Moved the workflows to `.github/workflows/`, the only folder GitHub runs workflows from.
- Fixed the `run-nam` typo (now `run-name`).
- Removed the conflicting `branches` / `branches-ignore` settings, which made GitHub reject the workflow.
- Updated retired action versions (`checkout@v2` to `v4`, `setup-python@v2` to `v5`, `upload-artifact@v2` to `v4`) and Python 3.8 to 3.12.

## Run locally (Mac)

```
python3 -m venv lab_01
source lab_01/bin/activate
pip install -r requirements.txt
pytest test/test_pytest.py
python -m unittest test.test_unittest
```