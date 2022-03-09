FROM ubuntu:latest

RUN apt update && apt install nginx vim -y
COPY index.html /var/www/html
