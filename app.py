import re

@app.route("/ocr", methods=["POST"])
def ocr():
    file = request.files.get("file")
    if not file:
        return {"error": "No file"}

    image = Image.open(file.stream)
    text = pytesseract.image_to_string(image, lang="jpn")

    # 改行を統一
    text = text.replace("\r", "")

    # 防衛〜キロまでを抽出（複数対応）
    pattern = r"防衛[\s\S]*?キロ"
    matches = re.findall(pattern, text)

    return {
        "raw": text,
        "blocks": matches
    }
