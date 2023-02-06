FROM python:3.11.1-alpine

WORKDIR /src
COPY . /src/
RUN python3 -m pip install /src
