# flask関連
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

# ログイン画面
@app.route("/")
def login_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

# if __name__ == "__main__":
#     app.run()