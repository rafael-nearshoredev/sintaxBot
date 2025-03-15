# Construir la imagen Docker
docker-build:
    docker-compose build

# Levantar el servicio con Docker Compose
docker-up:
    docker-compose up -d

# Ver logs del servicio
logs:
    docker-compose logs -f

# Detener y eliminar contenedores
docker-down:
    docker-compose down