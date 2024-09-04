from flask import Flask, jsonify
from model import chat_session

app = Flask(__name__)

@app.route('/predict/<delivery_times>', methods=['GET'])
def predict(delivery_times):
    # Send the delivery times to the chat session
    response = chat_session.send_message(delivery_times)
    return jsonify({"predicted_time": response.text})

if __name__ == '__main__':
    app.run(debug=True)