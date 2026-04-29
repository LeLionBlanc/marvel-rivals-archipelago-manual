#!/usr/bin/env python3
"""Pack the Manual Archipelago project into a .apworld file."""

import zipfile
import os
from pathlib import Path

GAME = "MarvelRivals"
CREATOR = "DrakeLeLionBlanc"
APWORLD_NAME = f"Manual_{GAME}_{CREATOR}.apworld"

# Files and directories to include in the package
INCLUDE = [
    "__init__.py",
    "container.py",
    "Data.py",
    "DataValidation.py",
    "Game.py",
    "Helpers.py",
    "Items.py",
    "Locations.py",
    "ManualClient.py",
    "Meta.py",
    "Options.py",
    "Regions.py",
    "Rules.py",
    "data",
    "hooks",
]

BASE_DIR = Path(__file__).parent
FOLDER_NAME = f"Manual_{GAME}_{CREATOR}"
OUTPUT_PATH = BASE_DIR / APWORLD_NAME


def pack():
    with zipfile.ZipFile(OUTPUT_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for item in INCLUDE:
            full_path = BASE_DIR / item
            if full_path.is_file():
                zf.write(full_path, f"{FOLDER_NAME}/{item}")
            elif full_path.is_dir():
                for file in full_path.rglob("*"):
                    if file.is_file() and not any(
                        part.startswith("__pycache__") for part in file.parts
                    ):
                        arcname = f"{FOLDER_NAME}/{file.relative_to(BASE_DIR)}"
                        zf.write(file, arcname)

    print(f"Packed: {OUTPUT_PATH}")


if __name__ == "__main__":
    pack()
