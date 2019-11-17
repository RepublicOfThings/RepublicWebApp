import yaml
from flask import Flask, render_template


CONFIG = yaml.load(open("config/config.yml"), Loader=yaml.SafeLoader)["app"]


PROXY_SCHEME = "https" if CONFIG.get("ssl", False) else "http"
PROXY_HOST = CONFIG["host"]
PROXY_PORT = CONFIG["port"]

app = Flask(__name__, template_folder="templates")

@app.route("/")
def smeiling():
    return render_template("index.html", target=f"{PROXY_SCHEME}://{PROXY_HOST}:{PROXY_PORT}/_login?dashboard=Vodafone")
