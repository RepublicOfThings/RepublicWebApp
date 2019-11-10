import yaml

# Setup Splunk config
SPLUNK = yaml.load(open("config/config.yml"), Loader=yaml.SafeLoader)["webapp"]["splunk"]

SPLUNK_SCHEME = "http"
SPLUNK_USERNAME = SPLUNK["username"]
SPLUNK_PASSWORD = SPLUNK["password"]
SPLUNK_HOST = SPLUNK["host"]
SPLUNK_PORT = SPLUNK["port"]

SPLUNK_BASE = f"{SPLUNK_SCHEME}://{SPLUNK_HOST}:{SPLUNK_PORT}"
# /en-US/account/insecurelogin?username={SPLUNK_USERNAME}&password={SPLUNK_PASSWORD}
# Setup proxy config
PROXY_SCHEME = "http"
PROXY_PORT = 5000
PROXY_HOST = "0.0.0.0"
PROXY_BASE = f"{PROXY_SCHEME}://{PROXY_HOST}:{PROXY_PORT}"
