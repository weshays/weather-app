FROM python:3.12

RUN apt update -yqq
RUN apt-get -q clean
RUN rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man

ENV PYTHONDONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
