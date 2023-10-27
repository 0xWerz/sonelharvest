from web.app import app


def start_web_interface():
    app.run('localhost', 80, debug=True)
