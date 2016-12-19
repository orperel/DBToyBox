#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory, jsonify, render_template
import MySQLdb

app = Flask(__name__)

# Serve static files like js, img, css etc.
@app.route('/<folder>/<fileName>')
def serveStatic(folder, fileName):
    if folder in ('js', 'img', 'css', 'lib', 'fonts', 'views'):
    	print type(folder), type(fileName)
        return send_from_directory(folder, fileName)
    
    return "404"

@app.route("/api/mosaic/")
def mosaic():
    l = []
    l.append({"event_category": "ART_EVENT", "event_name": "אומנות בכיכר1111", "event_description":"אומנות בכיכר הוא אירוע מיוחד במינו שקורה פעם בשנה בו עושים מלא מלא מלא אומנות בכיכר"})
    l.append({"event_category": "BOOK_EVENT", "event_name": "ספרים רבותיי", "event_description":
              "מה עוד נאמר על עם הספר..."})
    l.append({"event_category": "FOOD_EVENT", "event_name": "פסטיבל האוכל", "event_description":
              "מלא מלא אוכל בלה בלה בלה אוכל בלה אוכל."})    
    l.append({"event_category": "ART_EVENT", "event_name": "אומנות בכיכר", "event_description":"אומנות בכיכר הוא אירוע מיוחד במינו שקורה פעם בשנה בו עושים מלא מלא מלא אומנות בכיכר"})
    l.append({"event_category": "BOOK_EVENT", "event_name": "ספרים רבותיי", "event_description":
              "מה עוד נאמר על עם הספר..."})
    l.append({"event_category": "FOOD_EVENT", "event_name": "פסטיבל האוכל", "event_description":
              "מלא מלא אוכל בלה בלה בלה אוכל בלה אוכל."})    
    l.append({"event_category": "ART_EVENT", "event_name": "אומנות בכיכר", "event_description":"אומנות בכיכר הוא אירוע מיוחד במינו שקורה פעם בשנה בו עושים מלא מלא מלא אומנות בכיכר"})
    l.append({"event_category": "BOOK_EVENT", "event_name": "ספרים רבותיי", "event_description":
              "מה עוד נאמר על עם הספר..."})
    l.append({"event_category": "FOOD_EVENT", "event_name": "פסטיבל האוכל", "event_description":
              "מלא מלא אוכל בלה בלה בלה אוכל בלה אוכל."})    
    
    return jsonify(l)

@app.route("/api/city/")
def city():
    events = []
    events.append({"city_name": "Tel-Aviv", "event_id": 1, "event_category": "ART_EVENT", "event_name": "אומנות בכיכר1111", "event_description":"אומנות בכיכר הוא אירוע מיוחד במינו שקורה פעם בשנה בו עושים מלא מלא מלא אומנות בכיכר"})
    
    d = {"city_name": "Tel-Aviv", "events": events}
    
    return jsonify(d)

@app.route("/<path>")
@app.route("/<path>/")
def index(path):
	return send_from_directory("", "index.html")

@app.route("/")
def index2():
	return send_from_directory("", "index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)