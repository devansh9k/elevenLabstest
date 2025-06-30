from flask import Flask, render_template, request, jsonify
from elevenlabs import elevenlabs_tts
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/audio'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        text = request.form.get('text')
        voice_id = request.form.get('voice_id', 'u4HtmbcjVZVpiJLQ2GZn')
        model_id = request.form.get('model_id', 'eleven_multilingual_v2')
        output_file = request.form.get('output_file', 'output.mp3')
        stability = float(request.form.get('stability', 0.5))
        similarity_boost = float(request.form.get('similarity_boost', 0.5))

        # Make sure the output file has .mp3 extension
        if not output_file.lower().endswith('.mp3'):
            output_file += '.mp3'

        # Secure the filename
        output_file = secure_filename(output_file)
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_file)

        # Generate speech
        success = elevenlabs_tts.generate_speech(
            text=text,
            output_file=output_path,
            voice_id=voice_id,
            model_id=model_id
        )

        if success:
            return render_template(
                'index.html',
                result={
                    'success': True,
                    'output_file': f'/static/audio/{output_file}'
                }
            )
        else:
            return render_template(
                'index.html',
                result={
                    'success': False,
                    'error': 'Failed to generate speech'
                }
            )

    except Exception as e:
        return render_template(
            'index.html',
            result={
                'success': False,
                'error': str(e)
            }
        )

if __name__ == '__main__':
    app.run(debug=True, port=5003)
