from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/hello')
def hello():
    return render_template('01.hello.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('02.login.html')
    else:
        return '환영합니다.'

# 사용자가 localhost:5000/user/admin 라고 주소창에 입력    
@app.route('/user/<uid>')
def user(uid):
    return f'<h1>{uid}</h1>'

@app.route('/int/<int:number>')
def int_fn(number):
    return f'<h1>{number}</h1>'

@app.route('/float/<float:pi>')
def float_fn(pi):
    return f'<h1>{pi}</h1>'

# 파라미터를 여러개 입력할 수 있다
#사용자가 localhost:5000/add/4/and/5를 입력
@app.route('/add/<int:a>/and/<int:b>')
def add(a,b):
    return f'<h1>{a}+{b}={a+b}</h1>'

if __name__ == '__main__':
    app.run(debug=True)

