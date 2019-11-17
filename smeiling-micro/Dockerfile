FROM python:3.6.4

EXPOSE 8000

RUN useradd republic

RUN pip install flask pyyaml pyopenssl requests gunicorn

COPY /smeiling /app
COPY /config /app/config
WORKDIR /app

CMD gunicorn app:app --bind 0.0.0.0:8000 --log-level=info --threads=1 --workers=1 --timeout=5