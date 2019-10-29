# docker-miGest

Projeto opensource para gestão de folhas de obra de uma oficina

Editar o ficheiro ./docker/mysql.env.example e guardar como ./docker/mysql.env
Editar o ficheiro django/mlpbarreiro/sql.cnf.example e guardar como django/mlpbarreiro/sql.cnf

cd ./docker
docker-compose up

docker exec -it docker_python_migest /bin/bash
python /home/miguel/django/mlpbarreiro createsuperuser

start testing 127.0.0.1:8000

