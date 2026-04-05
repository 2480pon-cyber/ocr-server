FROM python:3.10

RUN apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-jpn

WORKDIR /app

COPY . .

RUN pip install flask pillow pytesseract

CMD ["python", "app.py"]
