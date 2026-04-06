from flask import Flask, jsonify, request, send_from_directory
import time
import json

app = Flask(__name__, static_folder='')

live_state = {
    'live': False,
    'started_at': None,
    'viewers': 0,
    'video_url': 'https://www.youtube.com/embed/YOUR_LIVE_VIDEO_ID?autoplay=1&mute=0'
}

# WebRTC signaling
signaling_data = {
    'offer': None,
    'answer': None,
    'candidates': []
}

@app.route('/')
def homepage():
    return send_from_directory('.', 'index.html')

@app.route('/live')
def watch_live():
    return send_from_directory('.', 'live.html')

@app.route('/media-panel/go-live')
def go_live_panel():
    return send_from_directory('media-panel', 'go-live.html')

@app.route('/status')
def status():
    if live_state['live'] and live_state['started_at']:
        elapsed = int(time.time() - live_state['started_at'])
        viewers = max(1, int(elapsed / 5) + 1)
        live_state['viewers'] = viewers
        return jsonify(
            live=True,
            viewers=viewers,
            duration=elapsed,
            video_url=live_state['video_url']
        )

    return jsonify(live=False, viewers=0, duration=0, video_url='')

@app.route('/start-live', methods=['POST'])
def start_live():
    if not live_state['live']:
        live_state['live'] = True
        live_state['started_at'] = time.time()
        live_state['viewers'] = 1
    return jsonify(
        live=True,
        viewers=live_state['viewers'],
        video_url=live_state['video_url']
    )

@app.route('/stop-live', methods=['POST'])
def stop_live():
    live_state['live'] = False
    live_state['started_at'] = None
    live_state['viewers'] = 0
    signaling_data['offer'] = None
    signaling_data['answer'] = None
    signaling_data['candidates'] = []
    return jsonify(live=False)

# WebRTC signaling endpoints
@app.route('/webrtc/offer', methods=['POST'])
def webrtc_offer():
    data = request.get_json()
    signaling_data['offer'] = data
    return jsonify({'status': 'ok'})

@app.route('/webrtc/answer', methods=['POST'])
def webrtc_answer():
    data = request.get_json()
    signaling_data['answer'] = data
    return jsonify({'status': 'ok'})

@app.route('/webrtc/candidate', methods=['POST'])
def webrtc_candidate():
    data = request.get_json()
    signaling_data['candidates'].append(data)
    return jsonify({'status': 'ok'})

@app.route('/webrtc/offer')
def get_offer():
    return jsonify(signaling_data['offer'] or {})

@app.route('/webrtc/answer')
def get_answer():
    return jsonify(signaling_data['answer'] or {})

@app.route('/webrtc/candidates')
def get_candidates():
    return jsonify(signaling_data['candidates'])

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    # For local development
    app.run(host='0.0.0.0', port=5000, debug=True)

    # For production deployment with gunicorn, use:
    # gunicorn app:app -b 0.0.0.0:$PORT
