from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import io

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

@app.route("/ocr", methods=["POST"])
def ocr():
    if "file" not in request.files:
        return "No file", 400

    file = request.files["file"]

    img = Image.open(io.BytesIO(file.read()))
    text = pytesseract.image_to_string(img, lang="jpn")

    return jsonify({
        "text": text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
