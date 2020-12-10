from flask import Flask
from view.api import testRoute

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello index"

app.register_blueprint(testRoute, url_prefix='')



if __name__ == "__main__":
    app.run(debug=True)