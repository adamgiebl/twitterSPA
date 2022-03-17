from email.mime import application
from email.policy import default
from bottle import run, get, view, static_file, error, post, request, redirect, default_app
import random
import uuid
import re


import globals
import users
import signup
import login
import home
import posts
import files
import db


@get("/global.css")
def _():
    return static_file("/static/css/global.css", root=".")

@get("/index.js")
def _():
    return static_file("/static/js/index.js", root=".")

@get("/favicon.ico")
def _():
    return static_file("/static/favicon.ico", root=".")

@get("/favicon-16x16.png")
def _():
    return static_file("/static/favicon-16x16.png", root=".")

@get("/favicon-32x32.png")
def _():
    return static_file("/static/favicon-32x32.png", root=".")

@get("/global.css.map")
def _():
    return static_file("/static/css/global.css.map", root=".")

@error(404)
@view("404")
def _(error):
    print(error)
    return



try:
    import production
    application = default_app()
except Exception as ex:
    print("Server running locally")

run(port=3333, reloader=True, debug=True)
