FROM --platform=linux/amd64 python:3.7-alpine
WORKDIR /usr/src/app

#COPY ./ ./

RUN git pull https://github.com/leemlb06pmi/docker-foursquare

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
