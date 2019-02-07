import csv
import datetime

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')
    
@app.route('/hi')
def hi():
    return "안녕, 단비!"
    
# 5월 20일부터 d-day를 출력하는 것을 만드세요
@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    vacation = datetime.datetime(2019, 5, 20)
    dday = vacation - today

    # return은 반드시 string으로 출력되어야한다! int나 float 등 다른 type은 안돼요!!
    # dday = datetime.timedelta(today, 2019.05.20.)
    return f'{dday.days}일 뒤에 놀러가자~~'
    
@app.route("/hi/<string:name>")
def greeting(name='홍길동'):
    return render_template('greeting.html', html_name=name)


# 세제곱의 결과를 출력해보자!
@app.route("/cube/<int:number>")
def tri(number):
    return f"{number}의 세 제곱은 {number**3} 입니다!"

    
@app.route("/movie")
def movie():
    movies = ["말모이", "극한직업", "국가부도의 날"]
    return render_template("movie.html", movies=movies)
    
@app.route("/google")
def google():
    return render_template("google.html")
    
    
@app.route("/naver")
def naver():
    return render_template("naver.html")
    
# 정보를 받는 페이지 1개, 받은 정보를 보여주는 페이지 1개 총 2개가 필요하다!
@app.route("/ping")
def ping():
    return render_template("ping.html")
    
    
@app.route("/pong")
def pong():
    name = request.args.get("name")
    msg = request.args.get("msg")
    return render_template("pong.html", name=name, msg=msg)


@app.route("/opgg")
def opgg():
    return render_template("opgg.html")

    
    
    
@app.route("/opgg_result")
def opgg_result():
    url = "http://www.op.gg/summoner/userName="
    
    username = request.args.get("opgg_username")
    
    # username = "hide on bush"
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, "html.parser")
    wins = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    losses = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses")

    return render_template("opgg_result.html", name=username, wins=wins.text, losses=losses.text)
    
    
    
    
    
@app.route("/opgg_hi")
def opgg_hi():
    return render_template("opgg_hi.html")

    
    
    
@app.route("/opgg_result_hi")
def opgg_result_hi():
    url = "http://www.op.gg/summoner/userName="
    
    username = request.args.get("opgg_username")
    
    # username = "hide on bush"
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, "html.parser")
    wins = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    losses = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses")

    return render_template("opgg_result_hi.html", name=username, wins=wins.text, losses=losses.text)
    
    
    
@app.route("/timeline")
def timeline():
    # 지금까지 기록되어있는방명록들('timeline2.csv')을 보여주자!
    with open("timeline2.csv", "r", encoding="utf-8", newline="") as f:
        read = csv.DictReader(f)
        timelines = []
        for row in read:
            timelines.append([row["username"]])
            timelines[-1].append(row["message"])

    
    return render_template('timeline.html',timelines=timelines)
    
    
@app.route("/timeline/create")
def timeline_create():
    username = request.args.get("username")
    message = request.args.get("message")
    
    # with open("timeline.csv", "a", encoding="utf-8", newline="") as f:
    #     f.write(f"{username}, {message}\n")
    
    with open("timeline2.csv", "a", encoding="utf-8", newline="") as f:
        write = csv.DictWriter(f, fieldnames=['username', 'message'])
        write.writerow({
            'username' : username,
            'message' : message
        })
        

        
    # return render_template("timeline_create.html", username=username, message=message)
    return redirect('/timeline')
    
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)