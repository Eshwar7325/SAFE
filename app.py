# app.py
from flask import Flask, render_template, request, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Serve the main page
@app.route('/')
def home():
    return render_template('main.html')

@app.route('/personal_info')
def personal_info():
    return render_template('personal Info.html')

@app.route('/about_us')
def about_us():
    return render_template('aboutUs.html')

# Handle incoming location data and broadcast it to all connected clients
@socketio.on('send_location')
def handle_send_location(data):
    print(f"Received location: {data}")
    emit('broadcast_location', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
