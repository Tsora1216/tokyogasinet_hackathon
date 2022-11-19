from flask import Flask,render_template ,request
import requests

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


@app.route("/change")
def change():
    money = 50
    url = 'https://toukyogasinethackathon.azurewebsites.net/api/HttpTrigger2?code=7KI8PBRSyakmetbKcuBjAeZLmU2BArfCBJ3SEQBfMPJNAzFu6MOBJQ==&name='+str(money)
    response = requests.get(url)
    print(response.text)
    num= response.text
    print(num)


    return render_template( 
        "index.html",
        title="サンプル",
        message = f"{num}"
    )

#プログラム起動
app.run(host="localhost",port=5000,debug=True)

