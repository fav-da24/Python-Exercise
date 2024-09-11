from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import pytesseract

# Set the tesseract executable path explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


from PIL import Image

app = Flask(__name__)

# MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="328426@MySQL",
    database="receipts"
)

cursor = db.cursor()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['receipt']
        if file:
            img = Image.open(file)
            text = pytesseract.image_to_string(img)
            # Process the text and extract the data you need
            cursor.execute("INSERT INTO receipts (data) VALUES (%s)", (text,))
            db.commit()
            return redirect(url_for('view_data'))
    return render_template('upload.html')


@app.route('/data')
def view_data():
    cursor.execute("SELECT * FROM receipts")
    results = cursor.fetchall()
    return render_template('data.html', results=results)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
