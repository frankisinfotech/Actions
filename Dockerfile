FROM ubuntu:latest

RUN apt update && apt install nginx && apt install vim -y
COPY index.html /var/www/html
