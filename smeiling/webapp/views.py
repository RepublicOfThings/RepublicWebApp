import yaml
import logging
from django.shortcuts import render
from django.http import HttpResponse

logging.basicConfig(level=logging.DEBUG)

CONFIG = yaml.load(open("config/config.yml"), Loader=yaml.SafeLoader)["app"]

logo = CONFIG.get("style", "/static/app/SmEILing.png")
dashboards = CONFIG.get("dashboards", {})
stylesheet = CONFIG.get("stylesheet", "app/content/republic.css")

BASE_URL = "{protocol}://{host}:{port}/{app}".format(protocol="https" if CONFIG.get("ssl", False) else "http",
                                                     host=CONFIG["host"],
                                                     port=CONFIG["port"],
                                                     app=CONFIG["name"])

META = {
    "css": stylesheet,
    "logo": logo["logos"],
    "app": CONFIG["name"],
    "base_url": BASE_URL,
    "dashboards": dashboards
}


def home(request):

    payload = {
        "title": "Home",
        **META
    }

    return HttpResponse(render(request, "pages/home/index.html", payload))


def about(request):
    payload = {
        "title": "About",
        **META
    }
    return HttpResponse(render(request, "pages/about/index.html", payload))


def dashboard(request, name):

    try:
        target_url = f"/proxy/_login?dashboard={name}"
        payload = {
            "title": f"{name}",
            "target": target_url,
            **META
        }
        return HttpResponse(render(request, "pages/dashboard/index.html", payload))
    except KeyError:
        return HttpResponse(b"No matching dashboard found.", status=404)
