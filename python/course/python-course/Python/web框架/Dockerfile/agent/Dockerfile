FROM centos7:1.4

RUN mkdir -pv /home/web-agent

ADD web-agent /home/web-agent

WORKDIR /home/web-agent/

CMD ["/usr/bin/python3","agent.py"]

