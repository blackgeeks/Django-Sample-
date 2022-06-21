FROM python:3.6

MAINTAINER Amad uddin

RUN apt-get update
ADD requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app
EXPOSE 8000
#CMD exec python manage.py runserver
#
CMD python manage.py runserver