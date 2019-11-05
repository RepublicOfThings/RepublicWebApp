import re
import os
import yaml
from django.shortcuts import render
from django.http import HttpResponse

config = yaml.load(open("config.yml"))

webapp = config["webapp"]
design = webapp["design"]
splunk = webapp["splunk"]

logos = [
        "https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/Vodafone_2017_logo.svg/1024px-Vodafone_2017_logo.svg.png"
    ]


def home(request):
    return HttpResponse(render(request, 'pages/home/index.html', {"title": "Home",
                                                                  "css": design["css"],
                                                                  "logo": design["logo"],
                                                                  "dashboards": webapp["dashboards"]}))


def about(request):
    return HttpResponse(render(request, 'pages/about/index.html', {"title": "About",
                                                                       "css": design["css"],
                                                                       "logo": design["logo"],
                                                                       "dashboards": webapp["dashboards"]}))


def dashboards(request, name):
    regex = re.compile('/dashboard/(.*)/')
    title = "Dashboard"
    dashboard_conf = {}
    for dashboard, conf in webapp["dashboards"].items():
        if regex.search(conf["url"]).group(1) == name:
            title = dashboard
            dashboard_conf = conf

    template = splunk.get("url_template")

    target = template.format(host=splunk.get("host"),
                             port=splunk.get("port"),
                             user=splunk.get("username"),
                             pwd=splunk.get("password"),
                             app=dashboard_conf.get("app"),
                             dash=dashboard_conf.get("dash"))

    return HttpResponse(render(request, 'pages/dashboard/index.html', {"title": title,
                                                                       "css": design["css"],
                                                                       "logo": design["logo"],
                                                                       "target": target,
                                                                       "dashboards": webapp["dashboards"]}))
