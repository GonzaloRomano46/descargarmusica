from flask import Flask, request, render_template, send_from_directory
import os
from pytube import YouTube

app = Flask(__name__)

def download_video_yt(url, path):
    try:
        yt = YouTube(url)
        yt.streams.get_highest_resolution().download(output_path=path)
        return "DESCARGA COMPLETA!"
    except Exception as e:
        return f"ERROR: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        path = request.form.get('path', 'C:/Users/Gonzalo/Desktop/musica descargada')
        message = download_video_yt(url, path)
        return render_template('index.html', message=message)
    return render_template('index.html')

@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


