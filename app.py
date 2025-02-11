from flask import Flask
from whitenoise import WhiteNoise

app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")  # Serve static files

@app.route("/")
def home():
    return "Hello, Flask is working!"

if __name__ == "__main__":
    app.run(debug=True)
