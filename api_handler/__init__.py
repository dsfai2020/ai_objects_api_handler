import requests

class Api_handler():
    """This is meant to be used in conjunction with the Ai_Objects Website.  It is an added communication layer."""
    def __init__(self):
        return

    def greet(self):
        print("Welcome to Api_handler")

    def ping(self):
        results=requests.get("https://flaskalone.herokuapp.com")
        print(results.content)


    
