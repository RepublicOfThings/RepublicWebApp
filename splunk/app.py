import requests
from flask import Flask, request, Response, redirect, render_template, url_for

import settings

# https://localhost:80/en-US/account/insecurelogin?username=vodademo&password=b98puxPJinkQ&return_to=app/rot_smart_homes_app/smeiling_dashboard_vodafone_demo_v10

app = Flask(__name__, template_folder="templates")
app.secret_key = settings.SECRET_KEY


session = requests.Session()


@app.route("/en-US/", defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("GET",))
def proxy(path: str):
    data = session.get(
        f"{settings.SPLUNK_BASE}/en-US/{path}", params=request.args
    ).content

    if path.endswith(".js"):
        return Response(data, mimetype="text/javascript")
    elif path.endswith(".css"):
        return Response(data, mimetype="text/css")
    elif (
        path.endswith(".json")
        or request.args.get("output_mode") == "json"
        or request.args.get("output_mode") == "json_cols"
    ):
        return Response(data, mimetype="text/json")
    return data


@app.route("/en-US/", defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("POST",))
def proxy_splunkd(path):

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

    return Response(j.content, status=j.status_code)


@app.route("/en-US/account/insecurelogin")
def insecure_login():
    response = session.get(
        f"{settings.SPLUNK_BASE}/en-US/account/insecurelogin", params=request.args
    )
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
    app.run(host=settings.PROXY_HOST, port=settings.PROXY_PORT, debug=True)
