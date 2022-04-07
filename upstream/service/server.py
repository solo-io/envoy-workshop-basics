from flask import Flask, request, abort
import random

app = Flask(__name__)


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):
    print(repr(u_path))
    
    if 'unreliable' in request.headers:
        # Fail the service 80% of the time
        fail = [True, True, True, True, False]
        if random.choice(fail):
            abort(500)

    return 'Hello back!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
