from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello, 徐國堂!</h1>"

def main():
    """啟動應用（教學用：啟用 debug 模式）"""
    # 在開發環境下使用 debug=True，部署時請關閉
    app.run(debug=True)

if __name__ == "__main__":
    main()