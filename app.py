from flask import Flask, request, jsonify
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    file = request.files["image"]
    img = Image.open(file.stream)

    text = pytesseract.image_to_string(img, lang="jpn")

    lines = text.split("\n")
    results = []

    for i in range(len(lines)):
        if "距離" in lines[i] and "キロ" in lines[i]:

            dist = lines[i]

            name = ""
            for j in range(1,6):
                if i-j < 0: continue
                t = lines[i-j]

                if any(x in t for x in ["防衛","ターゲット","集結","行軍","要塞","城","砦","ステーション"]):
                    continue

                if t.strip().isdigit():
                    continue

                if len(t.strip()) > 2:
                    name = t.strip()
                    break

            time = ""
            for j in range(1,6):
                if i-j < 0: continue
                t = lines[i-j]

                import re
                m = re.search(r"\d{2}:\d{2}:\d{2}", t)
                if m:
                    time = m.group()
                    break

            if name and time:
                results.append(f"{time} / {name} / {dist}")

    return jsonify({"result": results})

app.run(host="0.0.0.0", port=10000)
