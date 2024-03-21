#! /usr/bin/env python3

"""
Used to generate go/main.go
"""

import json
import logging
import os
from datetime import datetime, timezone

INPUT_FILE = "g2errors.json"
OUTPUT_FILE = "go/main.go"


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

# Create multi-line strings for output.

OUTPUT_HEADER = """// DO NOT EDIT.  This code is generated.
// Generated by: g2errors/bin/generate_go.py
"""

OUTPUT_HEADER += f"// Generated date: {datetime.now(timezone.utc).isoformat()}\n"

# noqa: E101, R801
OUTPUT_HEADER += """
package g2error

// ----------------------------------------------------------------------------
// Types
// ----------------------------------------------------------------------------

type G2ErrorTypeIds int

// ----------------------------------------------------------------------------
// "Category" errors
// One of these errors must be the last in each G2ErrorTypes value list.
// ----------------------------------------------------------------------------

type G2BadInputError struct {
	error
	G2ErrorTypeIds []G2ErrorTypeIds
}
type G2BaseError struct {
	error
	G2ErrorTypeIds []G2ErrorTypeIds
}
type G2ConfigurationError struct {
	error
	G2ErrorTypeIds []G2ErrorTypeIds
}
type G2RetryableError struct {
	error
	G2ErrorTypeIds []G2ErrorTypeIds
}
type G2UnrecoverableError struct {
	error
	G2ErrorTypeIds []G2ErrorTypeIds
}

// ----------------------------------------------------------------------------
// Detail errors
// ----------------------------------------------------------------------------

type G2DatabaseConnectionLostError struct{ error }
type G2DatabaseError struct{ error }
type G2LicenseError struct{ error }
type G2NotFoundError struct{ error }
type G2NotInitializedError struct{ error }
type G2RetryTimeoutExceededError struct{ error }
type G2UnhandledError struct{ error }
type G2UnknownDatasourceError struct{ error }

// ----------------------------------------------------------------------------
// Constants
// ----------------------------------------------------------------------------

const (
	G2Base G2ErrorTypeIds = iota
	G2BadInput
	G2Configuration
	G2Database
	G2DatabaseConnectionLost
	G2License
	G2NotFound
	G2NotInitialized
	G2Retryable
	G2RetryTimeoutExceeded
	G2Unhandled
	G2UnknownDatasource
	G2Unrecoverable
)

// ----------------------------------------------------------------------------
// Variables
// ----------------------------------------------------------------------------

// Message templates for g2engine implementations.
// Note: The lists of G2ErrorTypeIds are from innermost error to outer most error.
// Example:  #10 is G2RetryableError{G2RetryTimeoutExceededError{errors.New(message)}}
var G2ErrorTypes = map[int][]G2ErrorTypeIds{
"""  # noqa: E101, W191, R801

OUTPUT_FOOTER = """
}

// A list of all G2ErrorTypeIds.
var AllG2ErrorTypes = []G2ErrorTypeIds{
	G2BadInput,
	G2Base,
	G2Configuration,
	G2Database,
	G2DatabaseConnectionLost,
	G2License,
	G2NotFound,
	G2NotInitialized,
	G2Retryable,
	G2RetryTimeoutExceeded,
	G2Unhandled,
	G2UnknownDatasource,
	G2Unrecoverable,
}
"""  # noqa: E101,F541,W191,R801


with open(INPUT_FILE, encoding="utf-8") as input_file:
    errors = json.load(input_file)

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(OUTPUT_HEADER)
    for error_number, error_data in errors.items():
        OUTPUT_LINE = ""
        error_class = error_data.get("class")
        if error_class:
            CLASS_VARIABLE = error_class.removesuffix("Error")
            match CLASS_VARIABLE:
                case "G2":
                    CLASS_VARIABLE = "G2Base"
                case "G2NotFound":
                    CLASS_VARIABLE = "G2NotFound, G2BadInput"
                case "G2UnknownDatasource":
                    CLASS_VARIABLE = "G2UnknownDatasource, G2BadInput"
                case "G2DatabaseConnectionLost":
                    CLASS_VARIABLE = "G2DatabaseConnectionLost, G2Retryable"
                case "G2RetryTimeoutExceeded":
                    CLASS_VARIABLE = "G2RetryTimeoutExceeded, G2Retryable"
                case "G2Database":
                    CLASS_VARIABLE = "G2Database, G2Unrecoverable"
                case "G2License":
                    CLASS_VARIABLE = "G2License, G2Unrecoverable"
                case "G2NotInitialized":
                    CLASS_VARIABLE = "G2NotInitialized, G2Unrecoverable"
                case "G2Unhandled":
                    CLASS_VARIABLE = "G2Unhandled, G2Unrecoverable"
            OUTPUT_LINE = f"{error_number}: {{{CLASS_VARIABLE}}},"
            error_name = error_data.get("name")
            error_comment = error_data.get("comment")
            if error_name or error_comment:
                OUTPUT_LINE += f" // {error_name} - {error_comment}"
        if len(OUTPUT_LINE) > 0:
            OUTPUT_LINE += "\n"
            file.write(OUTPUT_LINE)
    file.write(OUTPUT_FOOTER)

# Epilog.

logging.info("-" * 80)
logging.info("--- %s} - End", os.path.basename(__file__))
logging.info("-" * 80)
