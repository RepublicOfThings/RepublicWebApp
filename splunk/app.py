import logging
import requests
from flask import Flask, request, Response, redirect

import settings

app = Flask(__name__)

session = requests.Session()

logger = logging.getLogger("SPLUNK-PROXY")
logging.basicConfig(level=logging.DEBUG)


@app.route('/en-US/', defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("GET", ))
def proxy(path: str):
    logger.debug(path)

    data = session.get(f"{settings.SPLUNK_BASE}/en-US/{path}", params=request.args).content

    if path.endswith(".js"):
        return Response(data, mimetype='text/javascript')
    elif path.endswith(".css"):
        return Response(data, mimetype='text/css')

    return data


@app.route('/en-US/', defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("POST", ))
def proxy_splunkd(path):
    url = f"{settings.SPLUNK_BASE}/en-US/{path}"

    data = request.values.to_dict()

    response = requests.post(url, json=data, headers=session.headers)

    return Response(response.content, status=response.status_code)


@app.route("/en-US/account/insecurelogin")
def login():
    response = session.get(f"{settings.SPLUNK_BASE}/en-US/account/insecurelogin", params=request.args)
    logger.debug("{0}{1} - VAGRANT".format(response.headers, response.cookies.get_dict()))
    if "return_to" in request.args:
        return_to = request.args.get("return_to")
        return redirect(f"{settings.PROXY_BASE}/en-US/{return_to}")
    else:
        return response.content


if __name__ == "__main__":
    app.run(host=settings.PROXY_HOST, port=settings.PROXY_PORT)
