#!/bin/sh

trap 'exit 0' SIGTERM
poetry run uvicorn sample_app:app --reload --host=0.0.0.0 --port=8000
