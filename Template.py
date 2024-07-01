from pathlib import Path
import os

list_of_files = [
    ".github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
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
