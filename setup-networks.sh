#!/bin/bash
# Recria as 7 redes Docker externas necessárias para o docker-compose.yml
set -e
docker network create --subnet=10.10.10.0/28  net_proxy
docker network create --subnet=10.10.10.16/28 net_app1
docker network create --subnet=10.10.10.32/28 net_db1
docker network create --subnet=10.10.10.48/28 net_app2
docker network create --subnet=10.10.10.64/28 net_db2
docker network create --subnet=10.10.10.80/28 net_app3
docker network create --subnet=10.10.10.96/28 net_db3
echo "Redes criadas com sucesso."
