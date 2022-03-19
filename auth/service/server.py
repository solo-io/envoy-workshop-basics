from flask import Flask, request, abort


app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def auth(path):
    if 'authorization' in request.headers:
        if request.headers['authorization'] == 'workshop':
                return 'Allowed!'
        
    abort(403)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
