from web.app import app


def start_web_interface():
    app.run('0.0.0.0', 80, debug=False)
