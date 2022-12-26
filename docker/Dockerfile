FROM python:3.11 as python-base

ARG USERNAME=jargon
ARG USER_UID=1000
ARG USER_GID=$USER_UID
ARG JARGON_ENV
ARG JARGON_APP
ARG PYTHON_VERSION=3.11
ARG POETRY_VERSION=1.3.1

ENV JARGON_ENV=${JARGON_ENV} \
    JARGON_APP=${JARGON_APP} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    # PIP
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # POETRY
    POETRY_VERSION=${POETRY_VERSION} \
    POETRY_HOME="/usr/local/pypoetry" \
    POETRY_CACHE_DIR="/var/cache/pypoetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    # PATHS
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


# --------------------------
# BASE IMAGE - BUILD
# - Base image for Development and Production
# --------------------------
FROM python-base as builder-base

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y \
        ca-certificates \
        libffi-dev \
        python-dev \
        build-essential \
        apache2 apache2-utils ssl-cert \
        libapache2-mod-wsgi-py3 \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR $PYSETUP_PATH

COPY poetry.lock pyproject.toml ./

RUN poetry install --only main

# --------------------------
# DEVELOPMENT BUILD
# - This is meant to be run in a .devcontainer but will
#   run as a development container.
# --------------------------
FROM python-base as development
ENV JARGON_ENV=dev

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y \
        vim \
        curl \
        git \
        iputils-ping \
    && apt clean -y && rm -rf /var/lib/apt/lists/*

COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

WORKDIR $PYSETUP_PATH

RUN poetry install

# We want the dev container to have root access so that we can install
# packages without having to restart the container every time.
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -s /bin/bash -m $USERNAME  \
    && apt-get update && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# This allows for bash history to remain between rebuilding the devcontainer
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && mkdir -p /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R $USERNAME /commandhistory \
    && echo "$SNIPPET" >> "/home/$USERNAME/.bashrc"

WORKDIR /workspace

USER $USERNAME

ENTRYPOINT ["/docker-entrypoint.sh"]

# --------------------------
# PRODUCTION BUILD
# --------------------------
FROM python-base as production
ENV JARGON_ENV=prod

COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

COPY ./docker/docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

RUN apt clean && rm -rf /var/lib/apt/lists/*

COPY ./$JARGON_APP /usr/app/$JARGON_APP
COPY ./config /usr/app/config

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -s /bin/bash -m $USERNAME \
    && mkdir -p /usr/app && chown -R $USERNAME /usr/app

WORKDIR /usr/app

USER $USERNAME

ENTRYPOINT ["/docker-entrypoint.sh"]
