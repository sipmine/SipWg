FROM python:3.9

WORKDIR /SipWg

ENV SERVER_PUBLIC_KEY=""
ENV SERVER_IP=""
ENV BOT_TOKEN=""
COPY . .

RUN pip install -r requirements.txt
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev
RUN apt-get install -y wireguard

RUN sqlite3 ac.db < createdb.sql

CMD python ./server.py
