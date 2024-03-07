import argparse
from flask import Flask, redirect, url_for, render_template
from database.keys import SECRET

# import the main_view blueprint which has all the application routes
from routes.view import main_view

# create the Flask app and set the secret key
app = Flask(__name__)
app.secret_key = SECRET
    
# create a route for the home page, and redirect to the main_view blueprint
@app.route("/")
def index():
    return redirect(url_for("main_view.home"))

# create a custom error page for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# register the main_view blueprint
app.register_blueprint(main_view)

# if the script is run directly, start the app
if __name__ == "__main__":
    # add a command line argument to run the app in debug mode
    parser = argparse.ArgumentParser()
    # if the --debug flag is passed, the app will run in debug mode
    parser.add_argument("--debug", action="store_true", help="Run in debug mode.")
    args = parser.parse_args()
    app.run(debug=args.debug)