from bottle import get, view, request, redirect, post
from globals import POSTS, authenticate
import uuid
import datetime

@get("/posts")
@view("posts")
def _():
    decoded = authenticate(request.get_cookie("jwt"))
    print(decoded)
    if decoded:
        filtered_posts = list(filter(lambda post: post["user"]["id"] == decoded["id"], POSTS))
        print(filtered_posts)
        return dict(posts=filtered_posts, user=decoded)
    else:
        return redirect('/login')

@post("/posts")
def _():
    decoded = authenticate(request.get_cookie("jwt"))
    if decoded:
        post_id = str(uuid.uuid4())
        POSTS.insert(0 ,{ "id": post_id, "user": { "id": decoded["id"], "name": f"{decoded['first_name']} {decoded['last_name']}", "hex_color": decoded["hex_color"] }, "content": request.forms.get("content"), "createdAt": datetime.datetime.now().timestamp() })
        return post_id
    else:
        return redirect('/login')

@post("/posts/delete/<post_id>")
def _(post_id):
    print(post_id)
    # VALIDATE
    for index, item in enumerate(POSTS):
        if item["id"] == post_id:
            POSTS.pop(index)
            return redirect('/posts')

    print("No item found")

    # No item found
    return redirect('/posts')