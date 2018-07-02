# Program to find out the inactive user

user = [
    {"username": "gaurav", "tweets": ["python is awesome"]},
    {"username": "piuli", "tweets": ["javaScript is awesome"]},
    {"username": "madhav", "tweets": []}
]
inactive_user = list(filter(lambda u: not u["tweets"], user))
active_user = list(filter(lambda u: u["tweets"], user))
username = list(map(lambda i: i["username"],
                    filter(lambda u: not u["tweets"], user)))
print("active user: {} \n inactive user: {}".format(active_user, inactive_user))
print("username: {}".format(username))
