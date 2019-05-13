#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Zheng <me@zxyle.cn>
# Date: 2019-03-29
# Desc: flask app

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    return render_template("index.html")


@app.route("/ip")
def view_origin():
    """Returns the requester's IP Address.
    ---
    tags:
      - Request inspection
    produces:
      - application/json
    responses:
      200:
        description: The Requester's IP Address.
    """

    return jsonify(origin=request.headers.get("X-Forwarded-For", request.remote_addr))


# @app.route("/headers")
# def view_headers():
#     """Return the incoming request's HTTP headers.
#     ---
#     tags:
#       - Request inspection
#     produces:
#       - application/json
#     responses:
#       200:
#         description: The request's headers.
#     """
#
#     return jsonify(get_dict('headers'))
#
#
# @app.route("/user-agent")
# def view_user_agent():
#     """Return the incoming requests's User-Agent header.
#     ---
#     tags:
#       - Request inspection
#     produces:
#       - application/json
#     responses:
#       200:
#         description: The request's User-Agent header.
#     """
#
#     headers = get_headers()
#
#     return jsonify({"user-agent": headers["user-agent"]})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
