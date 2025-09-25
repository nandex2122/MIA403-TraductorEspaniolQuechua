from flask import Flask, render_template, request
from translator import translate_text

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        translation = translate_text(input_text)
    return render_template('index.html', translation=translation)

if __name__ == '__main__':
    app.run(debug=True)