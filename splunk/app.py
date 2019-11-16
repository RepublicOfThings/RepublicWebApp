import logging
import requests
from flask import Flask, request, Response, redirect, render_template, url_for

import settings

<<<<<<< HEAD
<<<<<<< HEAD
# https://localhost:80/en-US/account/insecurelogin?username=vodademo&password=b98puxPJinkQ&return_to=app/rot_smart_homes_app/smeiling_dashboard_vodafone_demo_v10

app = Flask(__name__, template_folder="templates")
app.secret_key = settings.SECRET_KEY

=======
app = Flask(__name__)
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
=======
app = Flask(__name__)
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.

session = requests.Session()

logger = logging.getLogger("SPLUNK-PROXY")
logging.basicConfig(level=logging.DEBUG)
<<<<<<< HEAD
=======

>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.


@app.route("/en-US/", defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("GET",))
def proxy(path: str):
<<<<<<< HEAD
<<<<<<< HEAD
    data = session.get(
        f"{settings.SPLUNK_BASE}/en-US/{path}", params=request.args
    ).content
=======
=======
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
    logger.debug(path)

    data = session.get(f"{settings.SPLUNK_BASE}/en-US/{path}", params=request.args).content
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.

    if path.endswith(".js"):
        return Response(data, mimetype="text/javascript")
    elif path.endswith(".css"):
<<<<<<< HEAD
        return Response(data, mimetype="text/css")
    elif (
        path.endswith(".json")
        or request.args.get("output_mode") == "json"
        or request.args.get("output_mode") == "json_cols"
    ):
        return Response(data, mimetype="text/json")
=======
        return Response(data, mimetype='text/css')

<<<<<<< HEAD
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
=======
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
    return data


@app.route("/en-US/", defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("POST",))
def proxy_splunkd(path):
<<<<<<< HEAD
<<<<<<< HEAD

    app.logger.info(session.cookies)

    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "X-Splunk-Form-Key": session.cookies["splunkweb_csrf_token_8000"],
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    j = session.post(
        f"{settings.SPLUNK_BASE}/en-US/{path}",
        data=request.values.to_dict(),
        verify=False,
        headers=headers,
    )
=======
    url = f"{settings.SPLUNK_BASE}/en-US/{path}"

    data = request.values.to_dict()

    response = requests.post(url, json=data, headers=session.headers)
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
=======
    url = f"{settings.SPLUNK_BASE}/en-US/{path}"

    data = request.values.to_dict()

    response = requests.post(url, json=data, headers=session.headers)
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.

    return Response(response.content, status=response.status_code)


@app.route("/en-US/account/insecurelogin")
<<<<<<< HEAD
def insecure_login():
    response = session.get(
        f"{settings.SPLUNK_BASE}/en-US/account/insecurelogin", params=request.args
    )
=======
def login():
    response = session.get(f"{settings.SPLUNK_BASE}/en-US/account/insecurelogin", params=request.args)
    logger.debug("{0}{1} - VAGRANT".format(response.headers, response.cookies.get_dict()))
<<<<<<< HEAD
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
=======
>>>>>>> parent of 4d24938... Added smeiling, fixed proxy.
    if "return_to" in request.args:
        return_to = request.args.get("return_to")
        return redirect(f"{settings.PROXY_BASE}/en-US/{return_to}")
    else:
        return response.content


@app.route("/login")
def login():
    return redirect(url_for("insecure_login"))


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/ping")
def ping():
    return "OK"


if __name__ == "__main__":
    app.run(host=settings.PROXY_HOST, port=settings.PROXY_PORT)
