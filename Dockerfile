FROM ubuntu:18.04
ENV LANG C.UTF-8
MAINTAINER Dockerfiles

# Install required packages and remove the apt packages cache when done.
RUN apt update && apt install -y vim less python3.6 python3.6-dev python3-pip nginx supervisor

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app.conf /etc/supervisor/conf.d/

# COPY requirements.txt and RUN pip install BEFORE adding the rest of your code, this will cause Docker's caching mechanism
# to prevent re-installing (all your) dependencies when you made a change a line or two in your app.

COPY Keygene/requirements.txt /home/docker/code/Keygene/
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /home/docker/code/Keygene/requirements.txt \
&& sed -i.bak '35,37d' /usr/local/lib/python3.6/dist-packages/django/db/backends/mysql/base.py \
&& sed -i.bak 's/query.decode/query.encode/' /usr/local/lib/python3.6/dist-packages/django/db/backends/mysql/operations.py

# add (the rest of) our code
COPY . /home/docker/code/
WORKDIR /home/docker/code/Keygene
EXPOSE 8000 80
CMD supervisord -n


