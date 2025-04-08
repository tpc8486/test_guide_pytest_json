## pytest-test-guide-json

A Python package to convert `pytest` test results into a **JSON format compatible with [test.guide](https://www.tracetronic.com/products/testguide/)** by TraceTronic.

## 📘 Overview

**test.guide** by TraceTronic is a powerful tool for managing and analyzing automated test results. However, it does **not natively support `pytest`** output.

This package bridges the gap by:

- Collecting test results from `pytest`
- Converting them into a structured JSON format
- Ensuring full compatibility with test.guide’s expected JSON schema

## 🚀 Features

- Easy integration with existing `pytest` test suites
- Generates test.guide-compatible JSON reports
- Captures test case hierarchy, verdicts (`PASSED`, `FAILED`, `ERROR`, `INCONCLUSIVE`, etc.), durations, and more
- Supports nested folder/test structures for proper grouping in test.guide

## 🧪 Example Usage

1. **Install the package**:
```bash
pip install test-guide-pytest-json
```
2. **Create a .env file in the root of your project to store metadata**:
```env
PROJECT_NAME=my_project
ECU_NAME=my_ecu
ECU_VERSION=0.0.1
```

3. **Run your tests with pytest**:
```bash
# Generate timestamped file in the project root
pytest --json

# Generate report at a custom path
pytest --json some/path/report.json

# Short option
pytest -J some/path/report.json

# Run tests normally (no report generated)
pytest
```

