#!/bin/bash

# Bash script to run the test suite for the Pink Morsel Sales Visualiser
# Activates the virtual environment, runs pytest, and returns appropriate exit code

set -e

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Path to virtual environment
VENV_PATH="$SCRIPT_DIR/.venv"

# Check if virtual environment exists
if [ ! -d "$VENV_PATH" ]; then
    echo "Error: Virtual environment not found at $VENV_PATH"
    exit 1
fi

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Change to the project directory
cd "$SCRIPT_DIR"

# Run the test suite with pytest
echo "Running test suite..."
if python -m pytest test.py -v; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi
