#! /usr/bin/env python3

"""
Used to generate go/main.go
"""

import json
import logging
import os

INPUT_FILE = "szerrors.json"
OUTPUT_FILE = "szerrors_canonical.json"


def spaces_not_tabs():
    """Because tabs are used in OUTPUT_HEADER, linters get confused with spaces vs. tabs.  This solves it."""


# -----------------------------------------------------------------------------
# --- Main
# -----------------------------------------------------------------------------

# Set up logging.

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

logging.info("-" * 80)
logging.info("--- %s - Begin", os.path.basename(__file__))
logging.info("-" * 80)

with open(INPUT_FILE, encoding="utf-8") as input_file:
    errors = json.load(input_file)

# new_errors = {}
# for key, values in errors.items():
#     new_errors[key.zfill(5)] = values
# new_errors_pretty = json.dumps(errors, sort_keys=True, indent=4)

new_errors_pretty = json.dumps(
    {int(x): errors[x] for x in errors.keys()}, sort_keys=True, indent=4
)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(new_errors_pretty)

# Epilog.

logging.info("-" * 80)
logging.info("--- %s} - End", os.path.basename(__file__))
logging.info("-" * 80)
