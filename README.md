# health-check

# Image
$ docker pull bopems/healthcheck:latest

# docker-compose.yml
  health:
    image: bopems/healthcheck:latest
    container_name: health
    environment:
      - ENV_URL=http://192.168.99.100:8017/health
      - ENV_TRIES=5
      - ENV_TIMEOUT=30
      - ENV_INTERVAL=30

# Incluir etapa shell script no Jenkins

$ docker-compose up -d health
$ docker logs -f health | while IFS= read -r line; do if [ "$line" = "SUCCESS" ]; then echo "SUCCESS"; exit 0; else echo "UNABLED"; exit 1; fi; done
$ docker rm -f health

# ou 

$ docker run --env ENV_URL=http://192.168.99.100:8017/health --env ENV_TRIES=20 --env ENV_TIMEOUT=10 --env ENV_INTERVAL=30 --name health archib-health \
| archib-health | while IFS= read -r line; do if [ "$line" = "SUCCESS" ]; then echo "SUCCESS"; exit 0; else echo "UNABLED"; exit 1; fi; done
