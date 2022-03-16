from bottle import run, get, view, static_file, error, post, request, redirect
import random
import uuid
import re
from globals import USERS, POSTS, authenticate

@get("/")
@view("index")
def _():
    decoded = authenticate(request.get_cookie("jwt"))
    print(decoded)
    return dict(posts=POSTS, user=decoded)