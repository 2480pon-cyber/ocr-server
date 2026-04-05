from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "OK"

@app.route("/ocr", methods=["POST"])
def ocr():
    if "file" not in request.files:
        return "No file", 400

    file = request.files["file"]
    
    # とりあえず確認用
    return jsonify({
        "filename": file.filename
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
