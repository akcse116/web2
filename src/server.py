from flask import Flask, send_from_directory, session, request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    requester = request.remote_addr
    print("new visitor: " + requester)
    return send_from_directory('static', 'home.html')


@app.route('/about', methods=['GET'])
def about():
    return send_from_directory('static', 'about.html')


@app.route('/services', methods=['GET'])
def services():
    return send_from_directory('static', 'services.html')


# flask run --host=0.0.0.0
# app.run(app, port=8080)
if __name__ == "__main__":
    app.run(port=8080)
