from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import os

app = Flask(__name__)
CORS(app)  # Allow requests from frontend (different port)

# Simulated LangChain call
def call_langchain_agent(query):
    time.sleep(2)  # simulate delay
    return f"LangChain response for: {query}"

@app.route("/get-response", methods=["POST"])
def get_response():
    data = request.json
    query = data.get("query", "")
    response = call_langchain_agent(query)
    return jsonify({"response": response})

if __name__ == "__main__":
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
