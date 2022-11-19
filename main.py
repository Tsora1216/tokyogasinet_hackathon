from flask import Flask,render_template ,request

#Flaskのコンストラクタ
app = Flask(__name__,static_folder="static")


#ルーティング定義
@app.route("/")
def top():
    return render_template( 
        "sample.html",
        title="サンプル",
        message = "あいうえお"
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)
