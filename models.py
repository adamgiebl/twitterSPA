import uuid
import random

class User:
    def __init__(self, email, first_name, last_name, password):
        self.id = str(uuid.uuid4())
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.hex_color = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])