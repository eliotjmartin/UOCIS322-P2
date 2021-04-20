"""
Eliot Martin's flask API
"""

from flask import Flask, render_template, abort

app = Flask(__name__)


@app.route("/")
def hello():
    """
    main page visited when run
    """
    return "UOCIS docker demo!\n"


@app.route("/<path:name>")  # specify path to allow slashes (defaults to string which is problematic)
def redirect(name):
    """
    handle situations where user is not just looking for
    the home page. Check for 403 and 404 errors and
    redirect to appropriate html page in templates
    folder.
    """
    if '//' in name or '~' in name or '..' in name:  # check for forbidden characters
        abort(403)
    else:
        try:
            return render_template(name)  # first try to open html file from templates
        except:  # if render fails then the file isn't in templates folder -- abort
            abort(404)


@app.errorhandler(403)
def forbidden(e):
    """
    Handle 403 error message. Use render_template to look in templates folder
    for html files
    """
    return render_template("403.html"), 403  # follow with 403 to specify STATUS_CODE


@app.errorhandler(404)
def not_found(e):
    """
    Handle 404 error message. Use render_template to look in templates folder
    for html files
    """
    return render_template("404.html"), 404  # specify status code with 404


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
