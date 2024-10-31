FROM python:3.12-alpine
LABEL Author "Nemo Xiong <nemo@anzupop.com>"

RUN mkdir /chall
COPY ./chall.py /chall/chall.py
WORKDIR /chall

ENTRYPOINT [ "python", "/chall/chall.py" ]
