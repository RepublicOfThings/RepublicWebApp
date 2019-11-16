FROM python:3.6.4

EXPOSE 8000

RUN useradd republic

RUN pip install flask pyyaml pyopenssl requests gunicorn

COPY . /app
WORKDIR /app

CMD gunicorn app:app --bind 0.0.0.0:8000 --log-level=debug --threads=2 --workers=2 --timeout=5