import os
import hashlib
from datetime import datetime

from flask import Flask, render_template, jsonify


app = Flask(__name__)


# --------------------------------------------------
# OFFICIAL ADMISSION SOURCES
# --------------------------------------------------

SOURCES = [
    {
        "name": "KNRUHS",
        "full_name": "Kaloji Narayana Rao University of Health Sciences",
        "url": "https://www.knruhs.telangana.gov.in/all-notifications/"
    },
    {
        "name": "NTRUHS",
        "full_name": "Dr. NTR University of Health Sciences",
        "url": "https://drntr.uhsap.in/index/notification_admission"
    },
    {
        "name": "MCC",
        "full_name": "Medical Counselling Committee",
        "url": "https://mcc.nic.in/ug-medical-counselling/"
    },
    {
        "name": "TG EAPCET",
        "full_name": "Telangana EAPCET",
        "url": "https://tgeapcet.nic.in/"
    }
]


# --------------------------------------------------
# CREATE ALERT
# --------------------------------------------------

def make_alert(source):

    alert = {
        "source": source["name"],
        "priority": "HIGH",
        "category": "Official updates",
        "title": f"Check latest {source['name']} notifications",
        "summary": (
            "Open the official source for the latest "
            "admission and counselling updates."
        ),
        "date": datetime.now().strftime("%d %b %Y"),
        "url": source["url"]
    }

    alert["id"] = hashlib.md5(
        f"{alert['source']}|"
        f"{alert['title']}|"
        f"{alert['date']}".encode()
    ).hexdigest()[:12]

    return alert


# --------------------------------------------------
# CREATE ALERT LIST
# --------------------------------------------------

ALERTS = [make_alert(source) for source in SOURCES]


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def home():
    return render_template(
        "index.html",
        sources=SOURCES,
        alerts=ALERTS
    )


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.route("/healthz")
def healthz():
    return jsonify(
        ok=True,
        service="admission-alert"
    )


# --------------------------------------------------
# ALERT API
# --------------------------------------------------

@app.route("/api/alerts")
def get_alerts():
    return jsonify(
        alerts=ALERTS
    )


# --------------------------------------------------
# SCAN API
# --------------------------------------------------

@app.route("/api/scan")
def scan():
    return jsonify(
        ok=True,
        message=(
            "Scanner endpoint is reachable. "
            "Connect the worker for live scraping."
        )
    )


# --------------------------------------------------
# RUN LOCALLY
# --------------------------------------------------

if __name__ == "__main__":

    port = int(
        os.environ.get("PORT", 5000)
    )

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )
