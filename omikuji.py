from flask import Flask,render_template
import random

app=Flask(__name__)
@app.route("/")
def home():
    return render_template("omikuji.html")
@app.route("/omikuji")
def omikuji():
    result=random.choice(results)
    if result=="大吉":
        score=100
    elif result=="中吉":
        score=80
    elif result=="小吉":
        score=70
    elif result=="吉":
        score=60
    else:
        score=20

    if result=="大吉":
        love_results=["★★★★★","★★★★☆"]
    elif result=="中吉":
        love_results=["★★★★☆","★★★☆☆"]
    elif result=="小吉":
        love_results=["★★★☆☆","★★☆☆☆"]
    else:
        love_results=["★★☆☆☆","★☆☆☆☆"]
    love=random.choice(love_results)

    if result=="大吉":
        work_results=["★★★★★","★★★★☆"]
    elif result=="中吉":
        work_results=["★★★★☆","★★★☆☆"]
    elif result=="小吉":
        work_results=["★★★☆☆","★★☆☆☆"]
    else:
        work_results=["★★☆☆☆","★☆☆☆☆"]
    work=random.choice(work_results)

    if result=="大吉":
        money_results=["★★★★★","★★★★☆"]
    elif result=="中吉":
        money_results=["★★★★☆","★★★☆☆"]
    elif result=="小吉":
        money_results=["★★★☆☆","★★☆☆☆"]
    else:
        money_results=["★★☆☆☆","★☆☆☆☆"]
    money=random.choice(money_results)

    if result=="大吉":
        health_results=["★★★★★","★★★★☆"]
    elif result=="中吉":
        health_results=["★★★★☆","★★★☆☆"]
    elif result=="小吉":
        health_results=["★★★☆☆","★★☆☆☆"]
    else:
        health_results=["★★☆☆☆","★☆☆☆☆"]
    health=random.choice(health_results)
    
    return render_template(
        "omikuji.html",
        result=result,
        score=score,
        love=love,
        work=work,
        money=money,
        health=health
    )

results=["大吉","中吉","小吉","吉","凶"]
result=random.choice(results)
print(result)

if result=="大吉":
    print("今日は最高の日！")
elif result=="凶":
    print("今日は無理せずゆっくり過ごそう！")
else:
    print("今日もいい日になりそう！")

if result=="大吉":
    score=100
elif result=="中吉":
    score=80
elif result=="小吉":
    score=70
elif result=="吉":
    score=60
else:
    score=20
print("運勢ポイント:"+str(score))

if result=="大吉":
    love_results=["★★★★★","★★★★☆"]
elif result=="中吉":
    love_results=["★★★★☆","★★★☆☆"]
elif result=="小吉":
    love_results=["★★★☆☆","★★☆☆☆"]
else:
    love_results=["★★☆☆☆","★☆☆☆☆"]
love=random.choice(love_results)
print("恋愛："+love)

if result=="大吉":
    work_results=["★★★★★","★★★★☆"]
elif result=="中吉":
    work_results=["★★★★☆","★★★☆☆"]
elif result=="小吉":
    work_results=["★★★☆☆","★★☆☆☆"]
else:
    work_results=["★★☆☆☆","★☆☆☆☆"]
work=random.choice(work_results)
print("仕事："+work)

if result=="大吉":
    money_results=["★★★★★","★★★★☆"]
elif result=="中吉":
    money_results=["★★★★☆","★★★☆☆"]
elif result=="小吉":
    money_results=["★★★☆☆","★★☆☆☆"]
else:
    money_results=["★★☆☆☆","★☆☆☆☆"]
money=random.choice(money_results)
print("金運："+money)

if result=="大吉":
    health_results=["★★★★★","★★★★☆"]
elif result=="中吉":
    health_results=["★★★★☆","★★★☆☆"]
elif result=="小吉":
    health_results=["★★★☆☆","★★☆☆☆"]
else:
    health_results=["★★☆☆☆","★☆☆☆☆"]
health=random.choice(health_results)
print("健康："+health)

if __name__ =="__main__":
    app.run(debug=True)