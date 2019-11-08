cd .\server
docker-compose up -d

cd ..\client_a\
docker volume create input_output_a
docker-compose up -d

cd ..\client_b\
docker volume create input_output_b
docker-compose up -d

cd ..\