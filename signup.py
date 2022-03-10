from bottle import run, get, view, static_file, error, post, request, redirect, response
import re
import jwt
import json
from globals import REGEX_EMAIL, USERS, JWT_SECRET
from models import User

@get("/signup")
@view("signup")
def _():
    return

@post("/signup")
def _():
    if not re.match(REGEX_EMAIL, request.forms.get("email")):
        return "not valid"

    user_email = request.forms.get("email")
    first_name = request.forms.get("first_name")
    last_name = request.forms.get("last_name")
    password = request.forms.get("password")

    if not first_name or not last_name or not password:
        return "Invalid"

    user = User(user_email, first_name, last_name, password);
    
    USERS.append(user)

    user_without_password = {"id": user.id, "email": user.email, "first_name": user.first_name, "last_name": user.last_name, "hex_color": user.hex_color }

    encoded_jwt = jwt.encode(user_without_password, JWT_SECRET, algorithm="HS256")
    response.set_cookie("jwt", encoded_jwt)

    return redirect('/')