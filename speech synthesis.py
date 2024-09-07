import os
import uuid
from flask import Flask, jsonify, send_file
from gtts import gTTS

app = Flask(__name__)

# Function to generate a welcome message using Google Text-to-Speech (gTTS)
def generate_welcome_message():
    text = "Welcome to the University of Dar es Salaam ICT Reception. How can I assist you today?"
    tts = gTTS(text=text, lang='en', slow=False)

    # Generate unique file name for audio
    file_name = f"static/welcome_{uuid.uuid4()}.mp3"
    tts.save(file_name)
    
    return file_name

# API route to fetch the welcome message audio
@app.route('/api/welcome-audio', methods=['GET'])
def get_welcome_audio():
    try:
        # Generate and return the welcome audio file path
        file_path = generate_welcome_message()
        print(file_path)
        return jsonify({"audio_file": file_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API route to serve the audio file
@app.route('/static/<path:filename>', methods=['GET'])
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
