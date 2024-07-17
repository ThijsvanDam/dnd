# Dnd app

Iykwim DND app.

# DevContainer for Python and Svelte Development

This repository sets up a development environment using Docker and VS Code DevContainers for developing with Python (Flask) and Svelte. The setup includes optional configurations to switch between SQLite and PostgreSQL databases.

## Prerequisites

- Docker
- Visual Studio Code
- Remote - Containers extension for VS Code

## Getting Started


### 1. Setup the DevContainer

The development environment is defined using a `Dockerfile` and `docker-compose.yml`. The setup includes:

- Python with Flask and necessary dependencies.
- Node.js and npm for Svelte.
- `zsh` with `oh-my-zsh` and the Powerlevel10k theme for a nice terminal experience.

### 2. Open the Project in VS Code

1. Open VS Code.
2. Install the 'Dev Containers' extension - `ms-vscode-remote.remote-containers`
3. Restart VS Code
2. Use the "Remote - Containers" extension to open the project in the container.
    - Open Command Palette (`Ctrl+Shift+P`).
    - Search for something like `Reopen and rebuild in container` or select it on the notification you will get on the bottom right.


Info: The following commands will be run after the container is created to install the necessary dependencies:

- Python dependencies will be installed from `backend/requirements.txt`.
- Node.js dependencies will be installed for the Svelte project in the `frontend` directory.

### Key Files

- `.devcontainer/devcontainer.json`: Configuration for the VS Code DevContainer.
- `.devcontainer/Dockerfile`: Dockerfile to build the development container.
- `backend/`: Python backend project directory.
- `frontend/`: Svelte frontend project directory.

## Troubleshooting

If you encounter issues:

1. Ensure Docker is running and you have the latest version.
2. Ensure the Remote - Containers extension is installed in VS Code.
3. Check the output in the terminal for any errors during the build process.

Feel free to open an issue if you have any questions or need further assistance.

