from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
    <h1>🚀 Success!</h1>
    <p>Your Flask app is running inside a <b>Docker Container</b>.</p>
    <p>If you see this, your port mapping is working!</p>
    """


if __name__ == "__main__":
    # 0.0.0.0 is required for Docker containers
    app.run(host="0.0.0.0", port=5000)
