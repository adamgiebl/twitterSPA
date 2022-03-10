from bottle import get, view, request, post, redirect, response, auth_basic
import re

import jwt
from globals import REGEX_EMAIL, USERS, JWT_SECRET, COOKIE_SECRET

@get("/admin")
@view("admin")
def _():
    return dict(email=request.params.get("email"), name=f'{request.params.get("first-name")} {request.params.get("last-name")}')


@get("/login")
@view("login")
def _():
    return dict(error=request.params.get("error"), email=request.params.get("email"))

@post("/logout")
def _():
    response.delete_cookie("jwt")
    return redirect('/')

@post("/login")
def _():
    if not request.forms.get("email"):
        return redirect("/login?error=email")

    if not re.match(REGEX_EMAIL, request.forms.get("email")):
        return redirect("/login?error=email")

    password = request.forms.get("password")
    email = request.forms.get("email")

    print(password)
    
    if not password:
        return redirect(f"/login?error=user_password&email={email}")

    for user in USERS:
        if user.email == email and user.password == password:

            user_without_password = {"id": user.id, "email": user.email, "first_name": user.first_name, "last_name": user.last_name, "hex_color": user.hex_color }

            encoded_jwt = jwt.encode(user_without_password, JWT_SECRET, algorithm="HS256")
            response.set_cookie("jwt", encoded_jwt)

            print(encoded_jwt)
            
            return redirect("/")

    return redirect(f"/login?error=credentials&email={email}")