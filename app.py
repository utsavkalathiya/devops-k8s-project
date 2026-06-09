from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def home():
    # We will use this later to prove Helm can inject environment variables
    environment = os.getenv("ENVIRONMENT", "Development")
    hostname = socket.gethostname()
    
    return f"<h1>Automated Factory is Online! and working fine</h1><p>Environment: {environment}</p><p>Running on Pod/Container ID: {hostname}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)