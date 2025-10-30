from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

chatbot = ChatBot("ChatBot", read_only=False, 
                  logic_adapters=[
                      {
                          "import_path": "chatterbot.logic.BestMatch", 
                          "default_response": "I'm sorry, I do not understand.",
                          "maximum_similarity_threshold" : 0.9
                      }
                  ])

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/get_response")
def get_bot_response():
    user_text = request.args.get('msg')
    bot_response = chatbot.get_response(user_text)
    
    return jsonify({'response': str(bot_response)})


if __name__ == "__main__":
    app.run(debug=True)