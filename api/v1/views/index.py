#!/usr/bin/python3
"""
Creating Flask app: create route /status
on the object app_views that returns a JSON
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status')
def api_status():
    """
    route /status created
    :return: a JSON response
    """
    response = {'status': "OK"}
    return jsonify(response)


@app_views.route('/stats')
def get_stats():
    """
    endpoint that retrieves no. of each objs
    :return: JSON of all objs
    """
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User'),
    }

    return jsonify(stats)
