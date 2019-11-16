FROM python:3.6.4

EXPOSE 5000

RUN useradd republic

RUN pip install flask pyyaml pyopenssl requests gunicorn

COPY . /app
WORKDIR /app

CMD gunicorn app:app --bind 0.0.0.0:5000 --log-level=info --threads=2 --workers=2 --timeout=5