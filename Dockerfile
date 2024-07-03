# .devcontainer/Dockerfile

# Base image for the backend
FROM python:3.9-slim as backend

# Create the vscode user and group
RUN groupadd -g 1001 vscode \
    && useradd -u 1001 -g vscode -m vscode \
    && apt-get update && apt-get install -y sudo \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd

# Set the working directory for the backend
WORKDIR /app/backend

# Copy the backend requirements file
COPY backend/requirements.txt .

# Install backend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY backend/ .

# Base image for the frontend
FROM node:20 as frontend

# Create the vscode user and group
RUN groupadd -g 1001 vscode \
    && useradd -u 1001 -g vscode -m vscode \
    && apt-get update && apt-get install -y sudo \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd

# Set the working directory for the frontend
WORKDIR /app/frontend

# Copy the frontend package.json and package-lock.json files
COPY frontend/package*.json ./

# Install frontend dependencies
RUN npm install

# Copy the rest of the frontend code
COPY frontend/ .

# Build the frontend
RUN npm run build

# Final stage: combining backend and frontend
FROM python:3.9-slim

# Create the vscode user and group
RUN groupadd -g 1001 vscode \
    && useradd -u 1001 -g vscode -m vscode \
    && apt-get update && apt-get install -y sudo \
    && echo "vscode ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd
    
# Set the working directory
WORKDIR /app

# Copy backend from the backend build stage
COPY --from=backend /app/backend /app/backend

# Copy frontend build from the frontend build stage
COPY --from=frontend /app/frontend/build /app/frontend/build

# Expose the necessary ports
EXPOSE 8000 5000

# Install supervisord to manage processes
RUN apt-get update && apt-get install -y supervisor

# Copy supervisord configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Copy the entrypoint script
COPY entrypoint.sh /usr/local/bin/

# Make the entrypoint script executable
RUN chmod +x /usr/local/bin/entrypoint.sh

# Switch to the vscode user
USER vscode

# Start supervisord
CMD ["entrypoint.sh"]









