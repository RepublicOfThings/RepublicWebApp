import requests
from splunk.settings import SPLUNK_BASE, SPLUNK_USERNAME, SPLUNK_PASSWORD

query = {
    "auto_cancel": "90",
    "status_buckets": "0",
    "output_mode": "json",
    "earliest_time": "-24h@h",
    "latest_time": "now",
    "label": "search1",
    "preview": "true",
    "search": "search index=nbiottest sourcetype=sigfox:webthings | stats count by customer_id",
    "provenance": "UI:Dashboard:smeiling_dashboard_vodafone_demo_v10",
    "webframework.cache.hash": "java5:-25fc921d",
}

session = requests.Session()
r = session.get(
    f"{SPLUNK_BASE}/en-US/account/insecurelogin",
    params={"username": SPLUNK_USERNAME, "password": SPLUNK_PASSWORD},
)

d = session.get(
    f"{SPLUNK_BASE}/en-US/app/rot_smart_homes_app/smeiling_dashboard_vodafone_demo_v10"
)

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "X-Splunk-Form-Key": session.cookies["splunkweb_csrf_token_8000"],
    "Accept": "text/javascript, text/html, application/xml, text/xml, */*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

j = session.post(
    f"{SPLUNK_BASE}/en-US/splunkd/__raw/servicesNS/vodademo/rot_smart_homes_app/search/jobs",
    data=query,
    verify=False,
    headers=headers,
)

print(j.content)

# print(j.request.__dict__)
