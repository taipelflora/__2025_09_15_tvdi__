from flask import Flask, render_template  # 匯入 Flask 與模板渲染功能

app = Flask(__name__)  # 建立 Flask 應用程式實例

@app.route('/')  # 定義根路由 (root router)
def home():
    # 渲染樣版網頁
    return render_template('index.html')

if __name__ == '__main__':
    # 啟動 Flask 開發伺服器
    app.run(debug=True)
