from flask import Flask    # from the flask module import the flask class


app = Flask(__name__)     #create an instance of the flask class into app.
                        # app is now an "object"

@app.get("/")    # flask decorator that allows us to map a route to a view function
def index():     # Our view function
    return "<h1>Hello, world!</h1>"  # return statement.


# x = index() # function call


@app.get("/about")
def get_about():
    me = {
        "first_name": "David",
        "last_name": "DeSilvey",
        "hobbies": "Growing mushrooms",
        "active": True
    }
    return me
