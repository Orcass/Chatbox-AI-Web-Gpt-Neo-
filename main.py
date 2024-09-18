from email.policy import default
from flask import Flask, request, jsonify, render_template
from transformers import pipeline 
app = Flask(__name__)

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

@app.route("/")
def home():
    """
    This function is responsible for rendering the home page of the web application.
    Parameters: None
    Returns: render_template: A function call to render the 'index.html' template.
    """
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')  # Mengambil input user dari URL
    try:
        # Menggunakan GPT-Neo untuk menghasilkan respons
        response = generator(user_text, max_length=150, num_return_sequences=1)
        bot_response = response[0]['generated_text'].strip()
        
    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"})

    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7777)
    
print("openai._version_")
