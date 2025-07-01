from flask import Flask, request, render_template
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_path = None
    if request.method == 'POST':
        url = request.form['url']
        img = qrcode.make(url)
        qr_path = os.path.join('static', 'qr.png')
        img.save(qr_path)
    return render_template('index.html', qr_path=qr_path)

if __name__ == '__main__':
    app.run(debug=True)
