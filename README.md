# Projeto A2 - Questao 3 - Infraestrutura Docker

Tres aplicacoes web (WordPress, PHP, Django), cada uma com seu proprio banco
MySQL e GUI de administracao (phpMyAdmin), isoladas em redes Docker proprias
e expostas por um unico proxy reverso (Nginx), acessiveis via DNS
(app1.local, app2.local, app3.local).

## Como subir em uma nova maquina

1. Instalar Docker e Docker Compose.
2. Clonar este repositorio.
3. Criar as redes externas (uma vez so): ./setup-networks.sh
4. Subir os containers: docker compose up -d --build
5. Configurar DNS local (dnsmasq) apontando app1.local/app2.local/app3.local para o IP da maquina.
6. Testar com curl -I -H "Host: app1.local" http://localhost/
