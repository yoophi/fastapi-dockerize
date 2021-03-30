FROM python:3.8.1-alpine

# set work directory
WORKDIR /usr/src/app

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  CRYPTOGRAPHY_DONT_BUILD_RUST=1 \
  POETRY_VERSION=1.1.5

RUN apk add --no-cache gcc libffi-dev musl-dev openssl-dev

# install poetry
RUN pip install "poetry==$POETRY_VERSION"

# install dependencies
COPY poetry.lock pyproject.toml ./
COPY sample_app                 ./sample_app
COPY docker/entrypoint.sh       ./entrypoint.sh

RUN poetry install --no-root --no-dev
RUN source $(dirname $(poetry run which python))/activate
ENTRYPOINT "./entrypoint.sh"
