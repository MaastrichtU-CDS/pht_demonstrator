cd .\client_a\
docker-compose down

cd ..\client_b\
docker-compose down

cd ..\server
docker-compose down

cd ..\
docker volume prune -f