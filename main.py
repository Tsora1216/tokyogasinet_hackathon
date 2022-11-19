from flask import Flask,render_template ,request

#Flaskのコンストラクタ
app = Flask(__name__,static_folder="static")


#ルーティング定義
@app.route("/")
def top():
    
    return render_template( 
        "index.html",
        title="サンプル",
        message = "あいうえお"
    )
#プログラム起動
app.run(host="localhost",port=5000,debug=True)


@app.route("/sample")
def top2():
    
    num = 1+1;

    return render_template( 
        "index.html",
        title="サンプル",
        message = f"{num}"

    )
#プログラム起動
app.run(host="localhost",port=5000,debug=True)

