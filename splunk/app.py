import requests
from flask import Flask, request, Response, redirect, url_for, render_template

import settings

app = Flask(__name__)

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

    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "X-Splunk-Form-Key": session.cookies["splunkweb_csrf_token_8000"],
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    response = session.post(
        f"{settings.SPLUNK_BASE}/en-US/{path}",
        data=request.values.to_dict(),
        verify=False,
        headers=headers,
    )

    return Response(response.content, status=response.status_code)


@app.route("/en-US/account/insecurelogin")
def insecure_login():
    app.logger.debug(request.args)
    response = session.get(f"{settings.SPLUNK_BASE}/en-US/account/insecurelogin", params=request.args)
    if "return_to" in request.args:
        return_to = request.args.get("return_to")
        return redirect(f"{settings.PROXY_BASE}/en-US/{return_to}")
    else:
        return response.content


@app.route("/_login")
def login():

    dashboard = settings.DASHBOARDS[request.args["dashboard"]]

    return_to = f"app/{dashboard['app']}/{dashboard['name']}"

    args = {
        "username": settings.SPLUNK_USERNAME,
        "password": settings.SPLUNK_PASSWORD
    }

    response = session.get(f"{settings.SPLUNK_BASE}/en-US/account/insecurelogin", params=args)

    if response.status_code == 200:
        return redirect(f"{settings.PROXY_BASE}/en-US/{return_to}")
    else:
        return redirect(url_for("error", message=response.content, status=response.status_code))


@app.route("/_ping")
def ping():
    return


@app.route("/_error")
def error():
    message = request.args["message"]
    status = request.args["message"]
    return render_template("error.html", message=message, status=status)


if __name__ == "__main__":
    app.run(host=settings.PROXY_HOST, port=settings.PROXY_PORT)
