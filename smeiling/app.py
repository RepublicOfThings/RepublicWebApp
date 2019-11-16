from flask import Flask, render_template


SSL_ENABLED = False


app = Flask(__name__, template_folder="templates")


@app.route("/")
def smeiling():
    schema = "https" if SSL_ENABLED else "http"
    return render_template("index.html", target=f"{schema}://http://130.211.57.126/_login?dashboard=Vodafone")
