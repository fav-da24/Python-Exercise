from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdf/<filename>')
def serve_pdf(filename):
    return send_file(f'pdfs/{filename}', as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
