FROM centos7:1.4

RUN mkdir -pv /home/web-server

ADD web-server /home/web-server

WORKDIR /home/web-server/

CMD ["/usr/bin/python3","server.py"]

