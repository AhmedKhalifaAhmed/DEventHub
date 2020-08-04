#! bin/sh

# lock requirements
pipenv lock --requirements > requirements.txt
# Run build contianers
docker-compose -f docker-compose.prod.yml up -d --build