FROM python:3.6.4

EXPOSE 5000

RUN useradd republic

RUN pip install flask pyyaml pyopenssl requests

COPY . /app
WORKDIR /app

ENV FLASK_APP="app.py"

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0", "--port=5000"]