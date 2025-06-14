
from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/<target>')
def qr_clone(target):
    try:
        return send_from_directory('cloned_sites', f'{target}.html')
    except:
        return "Clone not found", 404

if __name__ == '__main__':
    app.run(debug=True)
