FROM ubuntu:latest

COPY ./src/* /code/
COPY ./Pipfile /code/
WORKDIR /code
RUN apt-get update && \
    apt-get install -yq libpython3-dev python3-pip && \
    pip3 install pipenv && \
    pipenv install

CMD ["pipenv run python /code/main.py du"]