import jwt

POSTS = [
  { "id": "1", "user": {"id": "111", "name": "Vincent van Gogh", "hex_color": "#FF5733"}, "content": "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.", "createdAt": "1644681932"},
  { "id": "2", "user": {"id": "222", "name": "John Smith", "hex_color": "#3383FF"}, "content": "What do you call a fish wearing a bowtie? Sofishticated.", "createdAt": "1644682137"},
  { "id": "3", "user": {"id": "333", "name": "Barbra Johnson", "hex_color": "#AAEE55"}, "content": "What do you call a factory that makes okay products? A satisfactory.", "createdAt": "1644684010"}
]

USERS = []

REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'

JWT_SECRET = 'keykeykey'
COOKIE_SECRET = "mhhhhhmm....cookie!"

def authenticate(token):
    try:
        decoded = jwt.decode(token, JWT_SECRET, algorithms="HS256")
        return decoded
    except:
        return False
