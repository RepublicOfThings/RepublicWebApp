FROM python:3.6.4

EXPOSE 8000

RUN pip install --upgrade django==2.0.3 pyyaml gunicorn==19.9.0

COPY . /app
WORKDIR /app

ARG SECRET_KEY
ARG DEBUG_MODE=TRUE

ENV SECRET_KEY=$SECRET_KEY \
    DEBUG_MODE=$DEBUG_MODE

CMD gunicorn RepublicWebApp.wsgi:application --bind 0.0.0.0:8000