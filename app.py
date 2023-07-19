from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a  artificial intelligence expert"}]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')

    if user_message:
        bot_message = CustomChatGPT(user_message)
        return jsonify({'reply': bot_message})

    return jsonify({'error': 'Invalid request'}), 400

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

if __name__ == '__main__':
    app.run()
