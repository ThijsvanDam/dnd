
# Base image for the backend
FROM python:3.9-slim AS backend

# Set the working directory for the backend
WORKDIR /app/backend

# Copy the backend requirements file
COPY backend/requirements.txt .

# Install backend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend code
COPY backend/ .

# Base image for the frontend
FROM node:16 AS frontend

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

# Start supervisord
CMD ["entrypoint.sh"]
