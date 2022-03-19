from flask import Flask, request

app = Flask(__name__)


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    return 'Hello back!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
