# MCI-Sport Service.
# Copyright (C) 2022 MCI-Sport.
# This file is distributed under the same license as the MCI-Sport package.
# Sajad Rezvani <majidstic@gmail.com>, 2022.


# Build stage
FROM python:3.11-slim AS builder

ARG DEPLOYMENT_ENVIRONMENT='test'

# Set Environment configs
ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=1000 \
  POETRY_VERSION=1.4.2 \
  DEPLOYMENT_ENVIRONMENT=$DEPLOYMENT_ENVIRONMENT

WORKDIR /

RUN apt-get update && apt-get install -y gcc unzip netcat-traditional gettext libpq-dev

RUN pip install "poetry==$POETRY_VERSION"

# install production requirements
COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$DEPLOYMENT_ENVIRONMENT" == production && echo "--no-dev") --no-interaction --no-ansi

# Configure Timezone
ENV TZ=Asia/Tehran

RUN echo 'Configuring timezone:' $TZ \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezonero

## Final image
#FROM python:3.10-slim

# set common work directory

RUN addgroup --system app \
    && adduser --system --disabled-login --ingroup app --no-create-home --home /nonexistent --gecos "app" --shell /bin/false --uid 1001 app

WORKDIR /usr/app


# Mount sourse code
COPY . .

# In production stage `DEBUG` is always False!
ARG DEBUG=True

# Expose the port that Django use it
EXPOSE 8000

# Make entrypoint executable and run the entrypoint to start jobs, gunicorns, liveness
RUN cp /usr/app/entrypoint.sh .
RUN chmod +x /usr/app/entrypoint.sh
RUN mkdir -p /usr/app/logs

RUN chown app:app -R /usr/app

USER app

ENTRYPOINT ["sh", "/usr/app/entrypoint.sh"]

CMD ["gunicorn", "link_chaincloak_django.wsgi:application"]
