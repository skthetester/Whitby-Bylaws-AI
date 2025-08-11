#!/bin/bash
# Stop any running containers
docker-compose down

# Build and run in detached mode
docker-compose up --build -d

echo "Backend is running. Use 'docker-compose logs -f' to view logs."