import yaml

CONFIG = yaml.load(open("config/config.yml"), Loader=yaml.SafeLoader)["app"]

# Get dashboards
DASHBOARDS = CONFIG["dashboards"]

# Setup Splunk config
SPLUNK = CONFIG["proxy"]

SPLUNK_SCHEME = SPLUNK["scheme"]
SPLUNK_USERNAME = SPLUNK["username"]
SPLUNK_PASSWORD = SPLUNK["password"]
SPLUNK_HOST = SPLUNK["host"]
SPLUNK_PORT = SPLUNK["port"]

SPLUNK_BASE = f"{SPLUNK_SCHEME}://{SPLUNK_HOST}:{SPLUNK_PORT}"

# Setup proxy config
PROXY_NAME = SPLUNK["name"]
PROXY_SCHEME = "https" if CONFIG.get("ssl", False) else "http"
PROXY_PORT = CONFIG["port"]
PROXY_HOST = CONFIG["host"]
PROXY_BASE = f"{PROXY_SCHEME}://{PROXY_HOST}:{PROXY_PORT}"
