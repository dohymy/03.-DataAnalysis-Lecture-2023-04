from flask import Flask, render_template, request
import melon_util as mu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/melon', methods=['GET', 'POST'])
def melon():
    rank_list = mu.melon()
    return render_template('melon.html', rank_list=rank_list)

if __name__ == '__main__':
    app.run(debug=True)

