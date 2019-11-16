import time
import requests
import logging
from selenium import webdriver
from flask import Flask, request, Response
from bs4 import BeautifulSoup as Soup

import settings

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")

DRIVER = webdriver.Chrome(chrome_options=options)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>", methods=("GET",))
def proxy(path):
    return requests.get(f"http://37.48.244.182:8000/{path}").content


# @app.route("/", methods=("GET", ))
# def dashboard():
#     app = request.args.get("app")
#     dashboard = request.args.get("dashboard")
#     DRIVER.get("https://localhost:80/en-US/account/insecurelogin?username=vodademo&password=b98puxPJinkQ&return_to=app/rot_smart_homes_app/smeiling_dashboard_vodafone_demo_v10")
#     # url = "http://37.48.244.182:8000/en-US/account/insecurelogin?username=vodademo&password=b98puxPJinkQ&return_to=app/rot_smart_homes_app/smeiling_dashboard_vodafone_demo_v10"
#     time.sleep(7)
#     return DRIVER.page_source


# @app.route('/en-US', defaults={"path": ""})
# @app.route("/en-US/<path:path>", methods=("GET", ))
# def resource(path):
#     data = requests.get(f"http://{settings.HOST}:{settings.PORT}/en-US/{path}").content
#     if path.endswith("config"):
#         logging.debug("JSON content type for resource: %s" % path)
#         return Response(data, mimetype='text/json')
#     elif path.endswith(".css"):
#         return Response(data, mimetype='text/css')
#     elif path.endswith(".js"):
#         return Response(data, mimetype='text/javascript')
#     else:
#         logging.debug("Unknown content type for resource: %s" % path)
#         return data


if __name__ == "__main__":
    app.run(host=settings.PROXY_HOST, port=settings.PROXY_PORT)

import time
import json
import requests
import logging
from selenium import webdriver
from flask import Flask, request, Response, redirect, url_for
from bs4 import BeautifulSoup as Soup

import settings

app = Flask(__name__)

session = requests.Session()

logging.basicConfig(level=logging.DEBUG)


@app.route("/en-US/", defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("GET",))
def proxy(path):
    logging.debug(path)

    data = session.get(
        f"http://37.48.244.182:8000/en-US/{path}",
        params=request.args,
        headers=request.headers,
    ).content

    if path.endswith(".js"):
        return Response(data, mimetype="text/javascript")
    elif path.endswith(".css"):
        return Response(data, mimetype="text/css")

    return data


@app.route("/en-US/splunkd", defaults={"path": ""})
@app.route("/en-US/splunkd/<path:path>", methods=("POST",))
def proxy_splunkd(path):
    url = f"http://37.48.244.182:8000/en-US/splunkd/{path}"
    cookie = request.headers["Cookie"]
    logging.warn(request.cookies)
    data = json.dumps(request.values.to_dict())
    # headers = {
    #     "Cookie": "splunkd_8000=SU6DmgAED70Kf14jnBY1LgWx6uyctf9tkqVCkEXUS2rk2L^LMybyvIXTeR6ElKKEz17__y2CUqF_zqCNWmTs93mCeIEBbk6YjT3bm_obUfeK0laWeeD3OXHw_2S7nXw8GdDZSYL; splunkweb_csrf_token_8000=13763717025271043236; session_id_8000=f603e33d22334b8639b385959323ea258d8acd8a; token_key=13763717025271043236; experience_id=bcde0718-4476-af4c-56b2-dc94094bc14a"
    # }
    response = session.post(url, json=data, data=data, verify=False)

    # if response.status_code != 200:
    #     logging.error("Failed to post with {0} - code {1} ({2})".format(str(request.values.to_dict()), response.status_code, response.content))
    #     return Response(response.content, status=response.status_code)
    # else:
    #     logging.info("Successfully posted with {0}".format(str(request.values.to_dict())))
    #     # print(response.content)
    #     return Response(response.content, status=)
    # logging.debug(response.headers)
    # return Response(response.content, status=response.status_code, content_type=response.headers["Content-Type"])
    return Response(response.content, status=response.status_code)


@app.route("/en-US/account/insecurelogin")
def login():
    response = session.get(
        f"http://37.48.244.182:8000/en-US/account/insecurelogin", params=request.args
    )
    logging.debug(
        "{0}{1} - VAGRANT".format(response.headers, response.cookies.get_dict())
    )
    if "return_to" in request.args:
        return_to = request.args.get("return_to")
        logging.error(response.headers)
        return redirect(f"https://localhost:80/en-US/{return_to}")
    else:
        return response.content


if __name__ == "__main__":
    app.run(host=settings.PROXY_HOST, port=settings.PROXY_PORT)
import time
import json
import requests
import logging
from selenium import webdriver
from flask import Flask, request, Response, redirect, url_for
from bs4 import BeautifulSoup as Soup

import settings

app = Flask(__name__)

session = requests.Session()

logging.basicConfig(level=logging.DEBUG)


@app.route("/en-US/", defaults={"path": ""})
@app.route("/en-US/<path:path>", methods=("GET",))
def proxy(path):
    logging.debug(path)

    data = session.get(
        f"http://37.48.244.182:8000/en-US/{path}", params=request.args
    ).content

    if path.endswith(".js"):
        return Response(data, mimetype="text/javascript")
    elif path.endswith(".css"):
        return Response(data, mimetype="text/css")

    return data


@app.route("/en-US/splunkd", defaults={"path": ""})
@app.route("/en-US/splunkd/<path:path>", methods=("POST",))
def proxy_splunkd(path):
    url = f"http://37.48.244.182:8000/en-US/splunkd/{path}"
    cookie = request.headers["Cookie"]
    logging.warn(request.cookies)
    data = request.values.to_dict()
    # headers = {
    #     "Cookie": "splunkd_8000=SU6DmgAED70Kf14jnBY1LgWx6uyctf9tkqVCkEXUS2rk2L^LMybyvIXTeR6ElKKEz17__y2CUqF_zqCNWmTs93mCeIEBbk6YjT3bm_obUfeK0laWeeD3OXHw_2S7nXw8GdDZSYL; splunkweb_csrf_token_8000=13763717025271043236; session_id_8000=f603e33d22334b8639b385959323ea258d8acd8a; token_key=13763717025271043236; experience_id=bcde0718-4476-af4c-56b2-dc94094bc14a"
    # }
    response = requests.post(url, json=data, data=data, verify=False)

    if response.status_code != 200:
        logging.error(
            "Failed to post with {0} - code {1} ({2})".format(
                str(request.values.to_dict()), response.status_code, response.content
            )
        )
        return Response(response.content, status=response.status_code)
    else:
        logging.info(
            "Successfully posted with {0}".format(str(request.values.to_dict()))
        )
        # print(response.content)
        # return Response(response.content, mimetype="text/json")
    return Response(response.content, status=response.status_code)


# @app.route('/en-US/app', defaults={"path": ""})
# @app.route("/en-US/app/<path:path>", methods=("GET", ))
# def proxy_app(path):
#     return session.get(f"http://37.48.244.182:8000/en-US/app/{path}", params=request.args).content


@app.route("/en-US/account/insecurelogin")
def login():
    response = session.get(
        f"http://37.48.244.182:8000/en-US/account/insecurelogin", params=request.args
    )
    logging.debug(
        "{0}{1} - VAGRANT".format(response.headers, response.cookies.get_dict())
    )
    if "return_to" in request.args:
        return_to = request.args.get("return_to")
        # # return redirect(url_for("proxy", path=return_to, _scheme='https', _external=True))
        # print(f"https://localhost:80/en-US/{return_to}")
        return redirect(f"https://localhost:80/en-US/{return_to}")
    else:
        return response.content


if __name__ == "__main__":
    app.run(host=settings.PROXY_HOST, port=settings.PROXY_PORT)
