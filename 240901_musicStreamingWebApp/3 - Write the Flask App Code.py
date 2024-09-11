from flask import Flask, send_file, render_template_string
import os

app = Flask(__name__)

# Path to your music directory
MUSIC_DIR = "/path/to/your/music"

@app.route('/')
def index():
    # List all music files
    files = os.listdir(MUSIC_DIR)
    music_files = [f for f in files if f.endswith('.mp3')]
    
    # Simple HTML template to list and play music
    template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Music Streaming</title>
    </head>
    <body>
        <h1>Music Streaming</h1>
        {% for file in music_files %}
            <div>
                <p>{{ file }}</p>
                <audio controls>
                    <source src="{{ url_for('stream', filename=file) }}" type="audio/mpeg">
                    Your browser does not support the audio element.
                </audio>
            </div>
        {% endfor %}
    </body>
    </html>
    '''
    return render_template_string(template, music_files=music_files)

@app.route('/stream/<filename>')
def stream(filename):
    # Stream the music file
    return send_file(os.path.join(MUSIC_DIR, filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
