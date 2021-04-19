"""
Eliot Martin's flask API
"""

from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route("/")
def hello():
    '''
    main page visited when run
    '''
    return "UOCIS docker demo!\n"

@app.route("/<name>")
def redirect(name):
    '''
    handle situations where user is not just looking for 
    the home page
    '''
    if '//' in name or '~' in name or '..' in name:
        abort(403)
    else:
        try:
            return render_template(name)
        except:
            abort(404)

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
