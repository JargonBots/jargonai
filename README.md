# JargonAI README

## Environment Setup

### Using VSCode

1. Make sure that both of these are installedj
    1. `Docker`
    2. `Docker Compose`
2. Open the repository using VSCode.
3. Install `Docker` and `Dev Container` extensions.
4. `ctrl+shift+p` or `cmd+shift+p` then type `Reopen in container`

This should close VSCode for a second and start building the docker container

This repository is tailored to work seamlessly with Visual Studio Code but
the instructions below gives the general idea on how to setup the development environment
outside of VSCode.

### Follow these steps if not running in VSCode

Install `poetry` python dependency management

```shell
curl -sSL https://install.python-poetry.org | python3 -
```

In the `config/` directory
1. Make a copy of the `.env.example` and name it `.env`
    ```shell
    cp .env.example .env
    ```
2. Change the values for 
    1. `OPENAI_API_KEY` to your API key
    2. `DISCORD_BOT_TOKEN`
    3. `DISCORD_OAUTH2_URL`
3. Source the env file
    ```shell
    source config/.env
    ```
4. Install dependencies using: `poetry install`
5. Activate the new virtual environment: `poetry shell` 

## Build Docker image

```shell
docker-compose build 
```

## Run Instructions

```shell
docker-compose run ai-app
```

Running the app will produce output in the shell and write it to a file within the output directory.
The output directory will be created if it doesn't exist.
