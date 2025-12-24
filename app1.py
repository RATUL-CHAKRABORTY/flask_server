from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import os

app = Flask(__name__)
CORS(app)

# Store last interaction (TEMP storage)
last_data = {
    "query": "",
    "response": ""
}

def call_langchain_agent(query):
    time.sleep(2)
    return f"LangChain response for: {query}"

@app.route("/get-response", methods=["POST"])
def get_response():
    data = request.json
    query = data.get("query", "")
    response = call_langchain_agent(query)

    # save it
    last_data["query"] = query
    last_data["response"] = response

    return jsonify({"response": response})

@app.route("/", methods=["GET"])
def home():
    return f"""
    <html>
      <body>
        <h1>Last request from localhost</h1>
        <p><b>Query:</b> {last_data['query']}</p>
        <p><b>Response:</b> {last_data['response']}</p>
      </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
