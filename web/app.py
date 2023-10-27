from flask import Flask, request, jsonify, render_template, Response, redirect, url_for
from scripts.geojson import geojson
import json

app = Flask(__name__, static_folder="static",  template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/export", methods=['POST'])
def export():
    try:
        data = request.get_json()
        country, target, tags = data['country'], data['target'], data['tags']
        if not country:
            country = "DZ"
        if not target:
            target = "power"
        if tags[0] == '':
            no_tags = json.dumps({
                "error": "no tags to query recieved. Please enter the tags you want to query",
            })
            return Response(no_tags, 400, mimetype="application/json")

        geojson_data = geojson(country, target, tags)
    except Exception as e:
        print(e)
        error = json.dumps({"error": f'{e}'})
        return Response(error, 500, mimetype="application/json")

    return geojson_data
