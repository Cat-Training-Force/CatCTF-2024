FROM python:3.12-alpine
LABEL Author "Nemo Xiong <nemo@anzupop.com>"
# change to tuna
# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories
# Entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN mkdir /chall
# add chall user
RUN addgroup -S chall && adduser -S chall -G chall -h /home/chall/ -s /bin/bash
# Alpine: make password hash section in shadow not '!'
RUN echo "chall:$(tr -dc A-Za-z0-9 < /dev/urandom | head -c 20)" | chpasswd
# ownership
RUN chown -R chall:chall /chall
# switch to chall
USER chall
# RUN python -m pip config set global.index-url https://mirror.sjtu.edu.cn/pypi/web/simple
RUN python -m pip install flask flask-cors
USER root
COPY ./secret.txt /chall/secret.txt
COPY ./chall.py /chall/chall.py
COPY ./lk0.mp3 /lk0.mp3
COPY ./templates /chall/templates
RUN chown -R chall:chall /chall
USER chall
ENTRYPOINT [ "sh", "/entrypoint.sh" ]