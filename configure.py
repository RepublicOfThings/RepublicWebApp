import os
import yaml
import uuid
import logging

THREAD = str(uuid.uuid4()).replace("-", "")
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

config = yaml.load(open(PROJECT_DIR+"/webapp/static/app/config.yml"))

app_log = logging.getLogger(config.get("name"))

httpd_app = open(PROJECT_DIR+"/conf/httpd-app.conf").read()
httpd_prefix = open(PROJECT_DIR+"/conf/httpd-prefix.conf").read()

httpd_app = httpd_app.format(thread=THREAD,
                             GROUP="{GROUP}",
                             GLOBAL="{GLOBAL}",
                             path=config.get("path"),
                             app=config.get("base"),
                             project=config.get("app"))

httpd_prefix = httpd_prefix.format(app=config.get("base"),
                                   path=config.get("path"))

print(httpd_prefix)

print(httpd_app)

"""

python3 deploy.py --target=vodafone --api=v2 --defaults=true

1) Spawn:

.rtk_deployment/v2/vodafone/config.yml
.rtk_deployment/v2/vodafone/activate.py

2) Clone to directory.
3) Inject `config.yml` file into above dir.
4) Run `configure.py` on project. Changes names etc.
5) Run `activate.py` to add app to apache.
6) Restart server.
 
"""