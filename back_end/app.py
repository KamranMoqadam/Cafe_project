from flask import Flask, session, g, Blueprint
from back_end.core.utils import Router
from url import routes
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
router = Router(app, routes)

if __name__ == "__main__":
    app.run(debug=True)
