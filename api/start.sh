#!/bin/bash

# Create venv if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate venv and install dependencies if requirements.txt is newer than venv
if [ ! -f "venv/.deps_installed" ] || [ "requirements.txt" -nt "venv/.deps_installed" ]; then
    echo "Installing/updating dependencies..."
    source venv/bin/activate
    pip install -r requirements.txt
    touch venv/.deps_installed
fi

# Create config if it doesn't exist
if [ ! -f "config.py" ]; then
    echo 'LINK = "sqlite:///base"' > config.py
fi

# Start the API
source venv/bin/activate
python main.py --dev