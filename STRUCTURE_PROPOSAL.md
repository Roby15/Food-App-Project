# Project Folder Structure

This file documents the proposed project folder structure for the "Order Chaos Kitchen" challenge.

## Top-level

- data/
  - generated/
    - generated_orders.csv  # produced by the generator
  - sample_orders.csv
- reports/
  - order_quality_report.txt
- src/
  - data_generator.py
  - reader.py
  - cleaner.py
  - validator.py
  - analyzer.py
  - anomaly_detector.py
  - reporter.py
  - main.py
- tests/
  - test_validator.py
  - test_cleaner.py
  - test_analyzer.py
  - test_anomaly_detector.py
- docs/
  - design_notes.md
- scripts/
  - run_tests.sh
  - generate_data.sh
- .gitignore
- README.md

## Purpose of each folder

- `data/`: CSV inputs and generated datasets.
- `reports/`: human-readable output reports for the Operations Analyst.
- `src/`: implementation modules, organized into small responsibilities (generator, reader, cleaner, validator, analyzer, anomaly detector, reporter, and `main` CLI).
- `tests/`: unit tests using Python's `unittest` module.
- `docs/`: short design notes, data schema, and usage instructions.
- `scripts/`: convenience scripts for running tests and generating data.

## Quick commands to create the structure locally

```bash
mkdir -p data/generated reports src tests docs scripts
touch data/sample_orders.csv data/generated/generated_orders.csv reports/order_quality_report.txt
touch src/data_generator.py src/reader.py src/cleaner.py src/validator.py src/analyzer.py src/anomaly_detector.py src/reporter.py src/main.py
touch tests/test_validator.py tests/test_cleaner.py tests/test_analyzer.py tests/test_anomaly_detector.py
echo "__pycache__/" > .gitignore
```

Feel free to tell me if you want me to scaffold minimal starter code for the modules next.
