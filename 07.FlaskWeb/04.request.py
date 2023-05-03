from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')

# localhost:5000/area?pi=3.14&radius=5
# values는 GET, POST 둘 다 쓰이는 방식
@app.route('/area')                 # 아무런 얘기가 없으면 GET방식
def area():
    pi=request.args.get('pi')
    radius=request.values['radius'] # args말고 values를 쓰는 방법
    a = float(pi)*float(radius)**2
    return f'<h1>pi={pi}, radius={radius}, area={a}</h1>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:                           # method가 POST
        uid = request.form['uid']
        pwd = request.values['pwd'] # form말고 values를 쓰는 방법
        return f'<h1>uid={uid}, pwd={pwd}</h1>'

if __name__ == '__main__':
    app.run(debug=True)

