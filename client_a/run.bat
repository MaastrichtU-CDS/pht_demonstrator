docker volume create input_output_a
docker-compose up -d

REM docker run --rm -it ^
REM     -v input_output_a:/input_output ^
REM     -v %cd%\.ptm_client_config.json:/app/config.json ^
REM     --add-host localmaster:172.17.0.1 ^
REM     -v /var/run/docker.sock:/var/run/docker.sock ^
REM     jvsoest/ptm_client