import fbchat
from os import environ

# Log the user in
session = fbchat.Session.login(environ['EMAIL'], environ['PASSWORD'])


# Send a message to yourself
session.user.send_text("Hi me!")

# Log the user out
session.logout()