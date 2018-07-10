FROM python:alpine AS base
WORKDIR /server
COPY . /server
RUN apk --no-cache add cmake clang clang-dev make gcc g++ libc-dev linux-headers jpeg-dev zlib-dev py-pillow \
    && pip install pipenv \
    && pipenv install
ENTRYPOINT pipenv run python server.py