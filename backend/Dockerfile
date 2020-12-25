FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1  

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get -y install apt-utils binutils libproj-dev gdal-bin

RUN pip install --upgrade pip
COPY ./requirements-dev.txt /usr/src/app/requirements-dev.txt
RUN pip install -r requirements-dev.txt

COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh

COPY . /usr/src/app/

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]