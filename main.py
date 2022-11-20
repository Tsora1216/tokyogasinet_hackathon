from flask import Flask,render_template ,request
import requests
import random



#Flaskのコンストラクタ
app = Flask(__name__,static_folder="static")

#ルーティング定義
@app.route("/")
def top():
    global num
    num=0
    
    return render_template( 
        "sawano-1.html",
        title="自分で作る宝箱"
        #message = 0,
        #message2 = f"どんどん貯金しちゃおう！今の貯金が将来のあなたの幸せに🥰"
    )

comment10 = ["10円貯金しました！貯金してくれてありがとう😄","貯金偉いね！将来の君も喜んでるよ😊","積み重ねると車買えるかもよ😏","貯金おめでとう！積み重ねが大事だよ😎"]
comment50 = ["50円貯金しました！今日も一日お疲れ様😄","この積み重ねがいつか大きな夢の後押しに😎","貯金ありがとう！老後は安心して暮らせるね🥰","貯金お疲れ様！貯金は継続が大事だよ😉"]
comment100 = ["100円貯金しました！貯金おめでとう😄","貯金お疲れ様！今日はゆっくり休んでね😇","10回貯めれば、1000円になるよ🤔","貯金ありがとう！毎日頑張ってて、すごいよ😍"]
comment500 = ["500円貯金しました！将来の君も喜んでるよ🤭","いつか車買えるかも🚗","貯金頑張って、誕生日に美味しいもの食べよ🥳","貯金頑張ってて本当にえらい！将来のために頑張ろう😊"]


@app.route("/change1",methods=["POST"])
def change1():

    username = request.form["usernames"]

    return render_template( 
        "shake1.html",
        title="自分で作る宝箱",
        message = 0,
        message2 = f"どんどん貯金しちゃおう！今の貯金が将来のあなたの幸せに🥰",
        name = f"{username}"
    )


@app.route("/change2")
def change2():
    global num
    global comment10

    num = num + 10

    number = random.randint(0,3)

    return render_template( 
        "shake1.html",
        title="自分で作る宝箱",
        message = num,
        message2 = comment10[number]
    )


@app.route("/change3")
def change3():
    global num
    global comment50
    num = num + 50

    number = random.randint(0, 3)


    return render_template( 
        "shake1.html",
        title="自分で作る宝箱",
        message = num,
        message2 = comment50[number]
    )


@app.route("/change4")
def change4():
    global num
    global comment100
    num = num + 100

    number = random.randint(0, 3)

    return render_template( 
        "shake1.html",
        title="自分で作る宝箱",
        message = num,
        message2 = comment100[number]
    )


@app.route("/change5")
def change5():
    global num
    global comment500
    num = num+500

    number = random.randint(0, 3)


    return render_template( 
        "shake1.html",
        title="自分で作る宝箱",
        message = num,
        message2 = comment500[number]
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)

