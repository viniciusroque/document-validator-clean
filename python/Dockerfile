FROM python:3.10-slim

RUN useradd -ms /bin/bash python

USER python

ENV HISTFILE=/home/python/history/.bash_history

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app/python/src

CMD [ "tail", "-f", "/dev/null" ]