from flask import Flask
import os

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def home():
    return "Hello, World! This app is running on Heroku."

# Run the app
if __name__ == "__main__":
    # Heroku dynamically assigns the port, so use that if available
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
