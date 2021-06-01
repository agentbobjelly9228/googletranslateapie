
from flask import Flask, jsonify, request
from flask_cors import CORS
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
CORS(app)


translator = Translator()


@app.route('/')
def index():
    return 'things'


@app.route('/translate', methods=['POST', 'GET'])
def home():
  if request.method == 'POST':
    words = request.args['words']
    lang = request.args['lang']
    print(translator.translate(words, dest=lang).text)
    return jsonify({'response': translator.translate(words, dest=lang).text})
  else:
    return 'hello world'


@app.route('/en', methods=['POST', 'GET'])
def langs():
  if request.method == 'GET':
    langg = LANGUAGES
    langs = []
    codes = []
    for i in langg:
      codes.append(i)
      langs.append(langg[i])
    print(langs)
    print(codes)
    langs.remove('english')
    langs.insert(0, 'english')
    codes.remove('en')
    codes.insert(0, 'en')
    stuff = {'languages': langs, 'codes': codes}
    return jsonify(stuff)
  else:
    return 'hi there'


@app.route('/chin', methods=['POST', 'GET'])
def chin():
  if request.method == 'GET':
    langg = LANGUAGES
    langs = []
    codes = []
    for i in langg:
      codes.append(i)
      langs.append(langg[i])
    print(langs)
    print(codes)
    langs.remove('chinese (traditional)')
    langs.insert(0, 'chinese (traditional)')
    codes.remove('zh-tw')
    codes.insert(0, 'zh-tw')
    stuff = {'languages': langs, 'codes': codes}
    return jsonify(stuff)
  else:
    return 'hi there'


if __name__ == '__main__':
  app.run(debug=True)
