"""Ubuntu에서 실행하고, 다음 수업에서 컨테이너로 옮길 Flask 앱."""

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
