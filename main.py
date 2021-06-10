
from flask import Flask, jsonify, request
from flask_cors import CORS
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
CORS(app)


translator = Translator()
ur1 = 'https://tts.agentbobjelly.repl.co/?Query=For%20an%20outing%20that%20gets%20you%20up%20close%20and%20personal%20with%20wildlife,%20head%20to%20Shing%20Mun%20Country%20Park.%20As%20soon%20as%20you%20arrive,%20you%20will%20most%20likely%20be%20greeted%20by%20troops%20of%20Rhesus%20Macaques.%20It%20is%20worth%20reading%20the%20signs%20that%20provide%20clear%20direction%20on%20how%20to%20deal%20with%20these%20furry%20marauders.%20They%20are%20natural%20actors%20and%20more%20than%20happy%20to%20pose%20for%20pictures.%20A%20number%20of%20hikes%20are%20spread%20throughout%20the%20park,%20but%20the%20easiest%20and%20most%20popular%20is%20the%20one%20to%20the%20reservoir.%20The%203.4-kilometer%20trail%20is%20easy%2C%20and%20the%20walk%20across%20the%20dam%20is%20worth%20experiencing.%20For%20a%20bit%20more%20distance%20and%20exercise%2C%20consider%20walking%20to%20the%20top%20of%20the%20hill%2C%20nicknamed%20Monkey%20Hill.%20To%20access%20the%20park%2C%20take%20the%20MTR%20to%20Tsuen%20Wan%20station%20and%20take%20exit%20B1.%20Walk%20a%20short%20distance%20to%20catch%20minibus%20%2382%2C%20and%20get%20off%20at%20the%20park%20entrance'
ur2 = 'https://tts.agentbobjelly.repl.co/?Query=For%20an%20outing%20that%20gets%20you%20up%20close%20and%20personal%20with%20wildlife,%20head%20to%20Shing%20Mun%20Country%20Park.%20As%20soon%20as%20you%20arrive,%20you%20will%20most%20likely%20be%20greeted%20by%20troops%20of%20Rhesus%20Macaques.%20it%20Is%20worth%20reading%20the%20signs%20that%20provide%20clear%20direction%20on%20how%20to%20deal%20with%20these%20furry%20marauders.%20They%20are%20natural%20actors%20and%20more%20than%20happy%20to%20pose%20for%20pictures.%20A%20number%20of%20hikes%20are%20spread%20throughout%20the%20park,%20but%20the%20easiest%20and%20most%20popular%20is%20the%20one%20to%20the%20reservoir.%20The%203.4-kilometer%20trail%20is%20easy,%20and%20the%20walk%20across%20the%20dam%20is%20worth%20experiencing.%20For%20a%20bit%20more%20distance%20and%20exercise,%20consider%20walking%20to%20the%20top%20of%20the%20hill,%20nicknamed%20Monkey%20Hill.%20To%20access%20the%20park,%20take%20the%20MTR%20to%20Tsuen%20Wan%20station%20and%20take%20exit%20B1.%20Walk%20a%20short%20distance%20to%20catch%20minibus%20#82,%20and%20get%20off%20at%20the%20park%20entrance.'


@app.route('/')
def index():
    return str(ur1 == ur2)


@app.route('/translate', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return str(request)
        try:
            words = request.get_json['words']
            lang = request.get_json['lang']
        except Exception as e:
            return e
            lang = 'en'
        return "jsonify({'response': translator.translate(words, dest=lang).text})"
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
