# pytest-testguide-json

A Python integration package to convert `pytest` test results into a **JSON format compatible with [test.guide](https://www.tracetronic.com/products/testguide/)** by TraceTronic.

## 📘 Overview

TraceTronic's **test.guide** is a powerful platform for managing and analyzing test results. While it natively supports several tools and formats, it does **not currently support `pytest`** out of the box.

This package bridges that gap by:

- Collecting test results from `pytest`
- Converting them into a structured JSON format
- Ensuring full compatibility with test.guide's expected JSON schema

## 🚀 Features

- Plug-and-play with existing `pytest` suites
- Generates test.guide-compatible JSON reports
- Captures test case hierarchy, verdicts (`PASSED`, `FAILED`, `ERROR`, `INCONCLUSIVE`, etc.), durations, and more
- Supports nested folder/test structures to reflect logical grouping in test.guide

## 🧪 Example Usage

1. Install the package:

```bash
pip install test-guide-pytest-json
```

2. Run your `pytest` tests with the `--json-report` option:

```bash
pytest --json=report.json
```

3. Point to a directory containing your tests:

```bash
pytest .\tests\ --json=report.json
```