from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketIO = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketIO.on('mensaje')
def handle_mensaje(msg):
    print(msg)
    socketIO.emit('mensaje', msg)

if __name__ == "__main__":
    socketIO.run(app, debug=True)


