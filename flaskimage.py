from flask import Flask, send_from_directory

app = Flask(__name__)
# @app.route('C:\Users\aresh\Rasa\flask_images\images\100.jpg')
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory('C:/Users/aresh/Rasa/flask_images/images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
