
from flask import Flask, jsonify, request
thing = ''
try: 
  from flask_cors import CORS
  from googletrans import Translator, LANGUAGES
except Exception as e:
  things = e

app = Flask(__name__)
CORS(app)


translator = Translator()


@app.route('/')
def index():
    return things


# @app.route('/translate', methods=['POST', 'GET'])
# def home():
#   if request.method == 'POST':
#     words = request.args['words']
#     lang = request.args['lang']
#     print(translator.translate(words, dest=lang).text)
#     return jsonify({'response': translator.translate(words, dest=lang).text})
#   else:
#     return 'hello world'


# @app.route('/langs', methods=['POST', 'GET'])
# def langs():
#   if request.method == 'POST':
#     langg = LANGUAGES
#     langs = []
#     codes = []
#     for i in langg:
#       codes.append(i)
#       langs.append(langg[i])
#     print(langs)
#     print(codes)
#     stuff = {'languages': langs, 'codes': codes}
#     return jsonify(stuff)
#   else:
#     return 'hi there'


if __name__ == '__main__':
  app.run(debug=True)
