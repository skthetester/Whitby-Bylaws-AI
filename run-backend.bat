@echo off
REM Build and run the backend using Docker Compose (Windows)

echo Stopping any running containers...
docker-compose down

echo Building and starting containers...
docker-compose up --build

pause