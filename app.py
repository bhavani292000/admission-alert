import os
from flask import Flask, render_template, jsonify
from datetime import datetime
app=Flask(__name__)
SOURCES=[
{"name":"KNRUHS","full_name":"Kaloji Narayana Rao University of Health Sciences","url":"https://www.knruhs.telangana.gov.in/all-notifications/"},
{"name":"NTRUHS","full_name":"Dr. NTR University of Health Sciences","url":"https://drntr.uhsap.in/index/notification_admission"},
{"name":"MCC","full_name":"Medical Counselling Committee","url":"https://mcc.nic.in/ug-medical-counselling/"},
{"name":"TG EAPCET","full_name":"Telangana EAPCET","url":"https://tgeapcet.nic.in/"}
]
ALERTS=[{"source":s["name"],"priority":"HIGH","category":"Official updates","title":f"Check latest {s['name']} notifications","summary":"Open the official source for the latest admission and counselling updates.","date":datetime.now().strftime("%d %b %Y"),"url":s["url"]} for s in SOURCES]
@app.get("/")
def home(): return render_template("index.html",sources=SOURCES,alerts=ALERTS)
@app.get("/healthz")
def healthz(): return jsonify(ok=True,service="admission-alert")
@app.get("/api/alerts")
def alerts(): return jsonify(alerts=ALERTS)
@app.get("/api/scan")
def scan(): return jsonify(ok=True,message="Scanner endpoint is reachable. Connect the worker for live scraping.")
if __name__=="__main__": app.run(host="0.0.0.0",port=int(os.environ.get("PORT",5000)))
