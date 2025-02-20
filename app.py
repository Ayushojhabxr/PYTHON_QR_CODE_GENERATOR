from flask import Flask, render_template, request, send_file
import qrcode
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr')
def generate_qr():
    url = request.args.get('url')  # Fetch URL from GET request

    if not url:
        return "Invalid URL", 400

    # Generate QR Code
    qr = qrcode.make(url)
    
    # Save QR code in memory (BytesIO)
    img_io = io.BytesIO()
    qr.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
