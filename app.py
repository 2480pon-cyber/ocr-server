from flask import Flask, request, jsonify
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

@app.route("/ocr", methods=["POST"])
def ocr():
    if "file" not in request.files:
        return "No file", 400

    file = request.files["file"]

    # ここが重要
    image = Image.open(file.stream)

    # OCR実行（日本語）
    text = pytesseract.image_to_string(image, lang="jpn")

    return jsonify({
        "text": text
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
