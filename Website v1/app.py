from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)

@app.route('/video/<video_name>')
def video(video_name):
    # Standard-Präferenzen aus Cookies
    audio_enabled = request.cookies.get('audio_enabled', 'True') == 'True'
    subtitles_enabled = request.cookies.get('subtitles_enabled', 'True') == 'True'
    speed = float(request.cookies.get('speed', '1.0'))

    # Videoquelle abhängig vom Namen
    video_src = f"{video_name}.mp4"
    return render_template('video.html', video_src=video_src, audio=audio_enabled, subtitles=subtitles_enabled, speed=speed)

@app.route('/set_preferences', methods=['POST'])
def set_preferences():
    # Präferenzen speichern
    audio_enabled = request.form.get('audio_enabled') == 'true'
    subtitles_enabled = request.form.get('subtitles_enabled') == 'true'
    speed = request.form.get('speed', '1.0')
    resp = make_response(redirect(url_for('video', video_name=request.form.get('video_name'))))
    resp.set_cookie('audio_enabled', str(audio_enabled))
    resp.set_cookie('subtitles_enabled', str(subtitles_enabled))
    resp.set_cookie('speed', speed)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
