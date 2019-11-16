import yaml

SSL_ENABLED = False

CONF = yaml.load(open("config/config.yml"), Loader=yaml.SafeLoader)

# Get dashboards
DASHBOARDS = CONF["webapp"]["dashboards"]

# Setup Splunk config
SPLUNK = CONF["webapp"]["splunk"]

SPLUNK_SCHEME = "http"
SPLUNK_USERNAME = SPLUNK["username"]
SPLUNK_PASSWORD = SPLUNK["password"]
SPLUNK_HOST = SPLUNK["host"]
SPLUNK_PORT = SPLUNK["port"]

SPLUNK_BASE = f"{SPLUNK_SCHEME}://{SPLUNK_HOST}:{SPLUNK_PORT}"

# Setup proxy config
PROXY_SCHEME = "https" if SSL_ENABLED else "http"
PROXY_PORT = 80
PROXY_HOST = "130.211.57.126"
PROXY_BASE = f"{PROXY_SCHEME}://{PROXY_HOST}:{PROXY_PORT}"
