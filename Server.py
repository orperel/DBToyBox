#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory, jsonify
import MySQLdb

app = Flask(__name__)

# Serve static files like js, img, css etc.
@app.route('/<folder>/<fileName>')
def serveStatic(folder, fileName):
    if folder in ('js', 'img', 'css', 'lib', 'fonts'):
    	print type(folder), type(fileName)
        return send_from_directory(folder, fileName)
    
    return "ERROR"

@app.route("/mosaic/")
def mosaic():
    l = []
    l.append({"category": "ART_EVENT", "name": "אומנות בכיכר", "description":"אומנות בכיכר הוא אירוע מיוחד במינו שקורה פעם בשנה בו עושים מלא מלא מלא אומנות בכיכר"})
    l.append({"category": "BOOK_EVENT", "name": "ספרים רבותיי", "description":
              "מה עוד נאמר על עם הספר..."})
    l.append({"category": "FOOD_EVENT", "name": "פסטיבל האוכל", "description":
              "מלא מלא אוכל בלה בלה בלה אוכל בלה אוכל."})    
    l.append({"category": "ART_EVENT", "name": "אומנות בכיכר", "description":"אומנות בכיכר הוא אירוע מיוחד במינו שקורה פעם בשנה בו עושים מלא מלא מלא אומנות בכיכר"})
    l.append({"category": "BOOK_EVENT", "name": "ספרים רבותיי", "description":
              "מה עוד נאמר על עם הספר..."})
    l.append({"category": "FOOD_EVENT", "name": "פסטיבל האוכל", "description":
              "מלא מלא אוכל בלה בלה בלה אוכל בלה אוכל."})    
    l.append({"category": "ART_EVENT", "name": "אומנות בכיכר", "description":"אומנות בכיכר הוא אירוע מיוחד במינו שקורה פעם בשנה בו עושים מלא מלא מלא אומנות בכיכר"})
    l.append({"category": "BOOK_EVENT", "name": "ספרים רבותיי", "description":
              "מה עוד נאמר על עם הספר..."})
    l.append({"category": "FOOD_EVENT", "name": "פסטיבל האוכל", "description":
              "מלא מלא אוכל בלה בלה בלה אוכל בלה אוכל."})    
    
    return jsonify(l)

@app.route("/")
def index():
	return send_from_directory("", "index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000)