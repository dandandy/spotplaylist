FROM python:alpine as build

RUN apk add --update --no-cache g++ gcc libxslt-dev

WORKDIR /app

COPY . .

FROM build as lint

RUN pip install pylint && pylint .

FROM build

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]