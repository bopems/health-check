# health-check

# Image
$ docker pull bopems/healthcheck:latest

# Incluir etapa shell script no Jenkins

$ docker run --env ENV_URL=http://192.168.99.100:8017/health --env ENV_TRIES=20 --env ENV_TIMEOUT=10 --env ENV_INTERVAL=30 --name health archib-health \
| archib-health | while IFS= read -r line; do if [ "$line" = "SUCCESS" ]; then echo "SUCCESS"; exit 0; else echo "UNABLED"; exit 1; fi; done
