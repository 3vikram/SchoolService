FROM ubuntu
MAINTAINER Trivikram Rajendraprabhu

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y wget
WORKDIR /home/schoolapp/
RUN git config --global http.sslverify false
RUN git clone https://github.com/3vikram/SchoolService.git
WORKDIR /home/schoolapp/SchoolService/
RUN python3 -m pip install -r requirements.txt
CMD python3 SchoolAPI.py
