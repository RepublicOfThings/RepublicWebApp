FROM python:3.6.4

EXPOSE 8000

RUN useradd republic

RUN pip install --upgrade django==2.0.3 pyyaml gunicorn==19.9.0 beautifulsoup4

COPY /smeiling /app
COPY /config /app/config
WORKDIR /app


CMD gunicorn RepublicWebApp.wsgi:application --bind 0.0.0.0:8000 --log-level=debug --threads=1 --workers=1 --timeout=5