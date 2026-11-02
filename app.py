"""Serve the Health360 website through Flask on a Python-capable host."""
import json, os
from pathlib import Path
from flask import Flask, Response, jsonify, send_from_directory
BASE=Path(__file__).resolve().parent
DASH="https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Dashboard_Final_"
STORY="https://public.tableau.com/views/Health360_Clinical_Healthcare_Risk_Analysis/Health360_Patient_Risk_Lifestyle_Insights"
REPO="https://github.com/Git-SI-2206/Health360-Healthcare-Analytics"
app=Flask(__name__,static_folder=None)
@app.get("/")
def home():
 return Response((BASE/"index.html").read_text(encoding="utf-8"),mimetype="text/html")
@app.get("/assets/config.js")
def config():
 values={"dashboardUrl":os.getenv("TABLEAU_DASHBOARD_URL",DASH),"storyUrl":os.getenv("TABLEAU_STORY_URL",STORY),"repositoryUrl":os.getenv("GITHUB_REPOSITORY_URL",REPO)}
 return Response("window.HEALTH360_CONFIG = "+json.dumps(values)+";",mimetype="application/javascript")
@app.get("/assets/<path:name>")
def assets(name):
 if name=="config.js": return config()
 return send_from_directory(BASE/"assets",name)
@app.get("/healthz")
def healthz(): return jsonify(status="ok",service="health360")
if __name__=="__main__": app.run(host="0.0.0.0",port=int(os.getenv("PORT","5000")),debug=False)