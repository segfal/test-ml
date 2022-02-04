FROM postgres:13
ENV POSTGRES_PASSWORD password
ENV POSTGRES_USER postgres
ENV POSTGRES_DB social_network
RUN apt update && apt upgrade
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install build-essential
RUN apt  install -y libglib2.0-dev libpq-dev
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
