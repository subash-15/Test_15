from flask import Flask, jsonify
import time
 
app = Flask(__name__)
 
@app.route("/")
def index():
    return jsonify({
        "message": "Test_15",
        "timestamp": time.time()
    })
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
