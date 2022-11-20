from flask import Flask,render_template ,request
import requests


num=0


#Flaskのコンストラクタ
app = Flask(__name__,static_folder="static")

#ルーティング定義
@app.route("/")
def top():
    
    return render_template( 
        "shake1.html",
        title="Web版貯金箱",
        message = 0
    )


@app.route("/change2")
def change2():
    global num
    num = num + 10

    return render_template( 
        "shake1.html",
        title="Web版貯金箱",
        message = num
    )


@app.route("/change3")
def change3():
    global num
    num = num + 50


    return render_template( 
        "shake1.html",
        title="Web版貯金箱",
        message = num
    )


@app.route("/change4")
def change4():
    global num
    num = num + 100

    return render_template( 
        "shake1.html",
        title="Web版貯金箱",
        message = num
    )


@app.route("/change5")
def change5():
    global num
    num = num+500


    return render_template( 
        "shake1.html",
        title="Web版貯金箱",
        message = num
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)

