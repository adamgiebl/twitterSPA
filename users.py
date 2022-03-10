from bottle import run, get, view, static_file, error, post, request, redirect, auth_basic
import random
import uuid
import re

from globals import USERS, authenticate


@get("/users")
@view("users")
def _():
    decoded = authenticate(request.get_cookie("jwt"))
    print(decoded)
    if decoded:
      return dict(users=USERS, user=decoded)
    else:
      return redirect('/login')

    
