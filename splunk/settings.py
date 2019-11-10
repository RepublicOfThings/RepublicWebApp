import os
import yaml
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Setup Splunk config
SPLUNK = yaml.load(open("config/config.yml"), Loader=yaml.SafeLoader)["webapp"]["splunk"]

# Basic splunk variables
SPLUNK_SCHEME = "http"
SPLUNK_USERNAME = SPLUNK["username"]
SPLUNK_PASSWORD = SPLUNK["password"]
SPLUNK_HOST = SPLUNK["host"]
SPLUNK_PORT = SPLUNK["port"]

# Some handy URLs
SPLUNK_BASE = f"{SPLUNK_SCHEME}://{SPLUNK_HOST}:{SPLUNK_PORT}"
SPLUNK_LOGIN = None

# Setup proxy config...
PROXY_SCHEME = "https"
PROXY_PORT = os.environ["TARGET_PORT"]
PROXY_HOST = "localhost"
PROXY_BASE = f"{PROXY_SCHEME}://{PROXY_HOST}:{PROXY_PORT}"

SECRET_KEY = "testing"

# Setup logging...
logging.basicConfig(level=SPLUNK.get("log-level", logging.DEBUG))
PROXY_LOGGER = logging.getLogger("SPLUNK-PROXY")