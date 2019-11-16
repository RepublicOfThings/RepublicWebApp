<<<<<<< HEAD
<<<<<<< HEAD
import os
import uuid
import yaml

APP_NAME = os.environ["APP_NAME"]

ENABLE_PROXY_SSL = True
ENABLE_SPLUNK_SSL = False

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
=======
import yaml
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
=======
import yaml
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.

# Setup Splunk config
SPLUNK = yaml.load(open("config/config.yml"), Loader=yaml.SafeLoader)["webapp"][
    "splunk"
]

<<<<<<< HEAD
<<<<<<< HEAD
# Basic splunk variables
SPLUNK_SCHEME = "http" if not ENABLE_SPLUNK_SSL else "https"
=======
=======
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
SPLUNK_SCHEME = "http"
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
SPLUNK_USERNAME = SPLUNK["username"]
SPLUNK_PASSWORD = SPLUNK["password"]
SPLUNK_HOST = SPLUNK["host"]
SPLUNK_PORT = SPLUNK["port"]

SPLUNK_BASE = f"{SPLUNK_SCHEME}://{SPLUNK_HOST}:{SPLUNK_PORT}"
<<<<<<< HEAD
<<<<<<< HEAD
SPLUNK_LOGIN = None

# Setup proxy config...
PROXY_SCHEME = "http" if not ENABLE_PROXY_SSL else "https"
PROXY_PORT = os.getenv("TARGET_PORT", 5000)
PROXY_HOST = "localhost"
PROXY_MOUNT = APP_NAME

PROXY_BASE = f"{PROXY_SCHEME}://{PROXY_HOST}:{PROXY_PORT}"

SECRET_KEY = os.getenv("SECRET_KEY", uuid.uuid4().hex)
=======
=======
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
# /en-US/account/insecurelogin?username={SPLUNK_USERNAME}&password={SPLUNK_PASSWORD}
# Setup proxy config
PROXY_SCHEME = "http"
PROXY_PORT = 5000
PROXY_HOST = "0.0.0.0"
PROXY_BASE = f"{PROXY_SCHEME}://{PROXY_HOST}:{PROXY_PORT}"
<<<<<<< HEAD
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
=======
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
