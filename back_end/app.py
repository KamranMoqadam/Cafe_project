from flask import Flask
from back_end.core.utils import Router
from url import routes
app = Flask(__name__)
router = Router(app, routes)

if __name__ == "__main__":
    app.run(debug=True)