import requests
from flask import Flask, request, Response, redirect

import settings

# http://localhost:5000/en-US/account/insecurelogin?username=vodademo&password=b98puxPJinkQ&return_to=app/rot_smart_homes_app/smeiling_dashboard_vodafone_demo_v10

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY

PROXY_LOGGER = settings.PROXY_LOGGER

session = requests.Session()


@app.route('/en-US/', defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("GET", ))
def proxy(path: str):
    PROXY_LOGGER.debug("proxy-handler %s" % session.__dict__)

    data = session.get(f"{settings.SPLUNK_BASE}/en-US/{path}", params=request.args).content

    if path.endswith(".js"):
        return Response(data, mimetype='text/javascript')
    elif path.endswith(".css"):
        return Response(data, mimetype='text/css')
    elif path.endswith(".json") or request.args.get("output_mode") == "json" or request.args.get("output_mode") == "json_cols":
        return Response(data, mimetype='text/json')
    return data


@app.route('/en-US/', defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("POST", ))
def proxy_splunkd(path):
    headers = {
        "X-Requested-With": "XMLHttpRequest",
        "X-Splunk-Form-Key": session.cookies["splunkweb_csrf_token_8000"],
        "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    j = session.post(f"{settings.SPLUNK_BASE}/en-US/{path}",
                     data=request.values.to_dict(),
                     verify=False,
                     headers=headers)

    return Response(j.content, status=j.status_code)


@app.route("/en-US/account/insecurelogin")
def login():
    response = session.get(f"{settings.SPLUNK_BASE}/en-US/account/insecurelogin", params=request.args)
    PROXY_LOGGER.info("login-handler %s" % session)
    if "return_to" in request.args:
        return_to = request.args.get("return_to")
        PROXY_LOGGER.info("redirect %s" % session)
        return redirect(f"{settings.PROXY_BASE}/en-US/{return_to}")
    else:
        return response.content


if __name__ == "__main__":
    app.run(host=settings.PROXY_HOST, port=settings.PROXY_PORT, debug=True)
