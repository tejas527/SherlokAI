from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot import CrimeChatbot
from parser import parse_user_case

app = Flask(__name__)
CORS(app)

bot = CrimeChatbot()

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    reply = bot.chat(user_msg)
    return jsonify({'response': reply})

@app.route('/start_case', methods=['POST'])
def start_case():
    case_text = request.json.get('case')
    parsed = parse_user_case(case_text)
    bot.set_case(parsed)
    return jsonify({'status': '✅ Case loaded.'})

if __name__ == '__main__':
    app.run(debug=True)
