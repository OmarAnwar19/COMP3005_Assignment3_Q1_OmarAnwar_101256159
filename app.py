import argparse
from flask import Flask, redirect, url_for, render_template
from database.keys import SECRET

from routes.view import main_view

app = Flask(__name__)
app.secret_key = SECRET
    
@app.route("/")
def index():
    return redirect(url_for("main_view.home"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

app.register_blueprint(main_view)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Run in debug mode.")
    args = parser.parse_args()
    app.run(debug=args.debug)