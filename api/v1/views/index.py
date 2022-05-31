#!/usr/bin/python3
"""Module view for index"""
from flask import jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/status')
def get_tasks():
    """Return the JSON status"""
    return jsonify({"status": "OK"})
