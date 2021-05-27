from googletrans import Translator, LANGUAGES
from flask import Flask, jsonify, request
from threading import Thread
from flask_cors import CORS

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


@app.route('/translate', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        words = request.args['words']
        lang = request.args['lang']
        print(translator.translate(words, dest=lang).text)
        return jsonify({'response': translator.translate(words, dest=lang).text})
    else:
        return 'hello world'


@app.route('/langs', methods=['POST', 'GET'])
def langs():
    if request.method == 'POST':
        langg = LANGUAGES
        langs = []
        codes = []
        for i in langg:
            codes.append(i)
            langs.append(langg[i])
        print(langs)
        print(codes)
        stuff = {'languages': langs, 'codes': codes}
        return jsonify(stuff)
    else:
        return 'hi there'


translator = Translator()

if __name__ == '__main__':
    app.run(debug=True)
