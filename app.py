
from flask import Flask, render_template, request, url_for, Response
import pytesseract
import cv2
from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


app = Flask(__name__)


@app.route('/' , methods=['GET', 'POST'] )
def homepage():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    try:
        imagefile = request.files.get('imagefile', '')
        print(imagefile)
        img = Image.open(imagefile)
        text = pytesseract.image_to_string(img)
        f = open("sample.txt", "a")
        f.truncate(0)
        f.write(text)
        f.close()
        return render_template('result.html', var=text)
    except:
        return "error"


if __name__ == '__main__':

    app.run(debug=True)

app.run(host='localhost', port=3000)
