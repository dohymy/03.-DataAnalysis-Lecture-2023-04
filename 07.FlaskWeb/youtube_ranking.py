from flask import Flask, render_template, request
import youtube_util as yu

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/youtube_ranking', methods=['GET', 'POST'])
def youtube_ranking():
    rank_list = yu.crawling()
    return render_template('youtube_ranking.html', rank_list=rank_list)

if __name__ == '__main__':
    app.run(debug=True)

