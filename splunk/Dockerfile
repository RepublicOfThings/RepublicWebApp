FROM python:3.6.4

EXPOSE 5000

RUN useradd republic

<<<<<<< HEAD
<<<<<<< HEAD
RUN pip install flask pyyaml pyopenssl requests gunicorn
=======
=======
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

RUN pip install flask pyyaml pyopenssl beautifulsoup4 requests selenium
<<<<<<< HEAD
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
=======
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.

COPY . /app
WORKDIR /app

<<<<<<< HEAD
<<<<<<< HEAD
CMD gunicorn app:app --bind 0.0.0.0:5000 --log-level=info --threads=2 --workers=2 --timeout=5
=======
=======
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
ENV FLASK_APP=app.py

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0", "--port=5000"]
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
