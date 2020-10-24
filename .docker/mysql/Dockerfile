FROM mysql:8

ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}

ADD ./mysql/databases.sql /docker-entrypoint-initdb.d

EXPOSE 3306