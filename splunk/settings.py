import yaml

# Setup Splunk config
SPLUNK = yaml.load(open("config/config.yml"), Loader=yaml.SafeLoader)["webapp"]["splunk"]

USERNAME = SPLUNK["username"]
PASSWORD = SPLUNK["password"]
HOST = SPLUNK["host"]
PORT = SPLUNK["port"]

SPLUNK_URL = f"http://{HOST}:{PORT}/en-US/account/insecurelogin?username={USERNAME}&password={PASSWORD}&return_to=app/"
# http://37.48.244.182:8000/en-US/account/insecurelogin?username=vodademo&password=b98puxPJinkQ&return_to=app/rot_smart_homes_app/smeiling_dashboard_vodafone_demo_v10

# Setup proxy config
PROXY_PORT = 5000
PROXY_HOST = "0.0.0.0"
