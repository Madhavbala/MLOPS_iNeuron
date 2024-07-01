from pathlib import Path
import os

list_of_files = [
    ".github/workflows/.gitkeep",  # Empty directory to keep GitHub workflows
    "src/__init__.py",  # Initialization file for source package
    "src/components/__init__.py",  # Initialization file for components package
    "src/components/data_ingestion.py",  # Script for data ingestion tasks
    "src/components/data_transformation.py",  # Script for data transformation tasks
    "src/components/model_trainer.py",  # Script for training machine learning models
    "src/components/model_evaluation.py",  # Script for evaluating machine learning models
    "src/pipeline/__init__.py",  # Initialization file for pipeline package
    "src/pipeline/training_pipeline.py",  # Script defining training pipeline steps
    "src/pipeline/prediction_pipeline.py",  # Script defining prediction pipeline steps
    "src/utils/__init__.py",  # Initialization file for utilities package
    "src/utils/utils.py",  # Utility functions for various tasks
    "src/logger/logging.py",  # Logging configuration and utilities
    "src/exception/exception.py",  # Custom exception classes and handling
    "tests/unit/__init__.py",  # Initialization file for unit tests
    "tests/integration/__init__.py",  # Initialization file for integration tests
    "init_setup.sh",  # Shell script for initial project setup
    "requirements.txt",  # Main requirements file for project dependencies
    "requirements_dev.txt",  # Additional requirements for development environment
    "setup.py",  # Script for packaging the project for distribution
    "setup.cfg",  # Configuration file for setup.py
    "pyproject.toml",  # Project metadata and dependencies configuration
    "tox.ini",  # Configuration file for tox testing tool
    "experiment/experiments.ipynb"  # Jupyter notebook for experimental code and analysis
]

def create_files(files):
    for file_path in files:
        filepath = Path(file_path)
        filedir = filepath.parent
        if not filedir.exists():
            filedir.mkdir(parents=True, exist_ok=True)

        if not filepath.exists() or filepath.stat().st_size == 0:
            with open(filepath, 'w') as f:
                print(f"Created file: {filepath}")

if __name__ == "__main__":
    create_files(list_of_files)
