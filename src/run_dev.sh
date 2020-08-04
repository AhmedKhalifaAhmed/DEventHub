#! bin/sh

# lock requirements
pipenv lock --requirements > requirements.txt

# Run build contianers
docker-compose -f docker-compose.dev.yml up --build

# Deleting volumes and data
docker-compose -f docker-compose.dev.yml down -v
